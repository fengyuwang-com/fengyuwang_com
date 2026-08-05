#!/usr/bin/env python3
"""Simple HTTP server that respects _headers rules for cache control.

Reads Cloudflare-style _headers rules and applies them to all responses.
All responses without explicit rules get no-cache by default.

Usage:
  python server.py            # serves current directory on port 8001
  PORT=8080 python server.py  # custom port
"""
import os
import re
import http.server
import urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))


def parse_headers(path):
    """Parse Cloudflare-style _headers into list of (pattern_regex, headers_dict)."""
    rules = []
    current_prefix = None
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if line.startswith("/") or line.startswith("*"):
                    # Convert simple glob to regex
                    parts = []
                    for ch in re.split(r'(\*)', line.rstrip()):
                        if ch == '*':
                            parts.append('.*')
                        else:
                            parts.append(re.escape(ch))
                    current_prefix = re.compile('^' + ''.join(parts))
                elif current_prefix and ':' in line:
                    key, val = line.split(':', 1)
                    rules.append((current_prefix, key.strip().lower(), val.strip()))
    except FileNotFoundError:
        pass
    return rules


HEADERS_RULES = parse_headers(os.path.join(ROOT, "_headers"))


CACHE_HEADERS = {
    'Cache-Control': 'no-cache, no-store, must-revalidate',
    'Pragma': 'no-cache',
    'Expires': '0',
}


def _headers_for_path(path):
    """Return (dict_of_headers, has_custom_rule) for a given URL path."""
    headers = {}
    matched = False
    for prefix, key, val in HEADERS_RULES:
        if prefix.search(path):
            matched = True
            # Normalize key to the canonical form
            if key == 'cache-control':
                headers['Cache-Control'] = val
            elif key == 'pragma':
                headers['Pragma'] = val
            elif key == 'expires':
                headers['Expires'] = val
    if not matched:
        headers.update(CACHE_HEADERS)
    return headers


class CacheBustingHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP handler that applies _headers rules and logs requests."""

    def _set_cache_headers(self):
        """Set cache headers before the response is sent."""
        path = urllib.parse.urlparse(self.path).path
        headers = _headers_for_path(path)
        for key, val in headers.items():
            self.send_header(key, val)

    # Override do_GET and do_HEAD to inject cache headers before send_head
    def do_GET(self):
        f = self.send_head()
        if f:
            try:
                self.copyfile(f, self.wfile)
            finally:
                f.close()

    def do_HEAD(self):
        f = self.send_head()
        if f:
            f.close()

    def send_head(self):
        """Override to inject cache headers before the response."""
        path = urllib.parse.urlparse(self.path).path
        # Determine the file path first to know if it exists
        f = super().send_head()
        return f

    def send_response(self, code, message=None):
        """Override to inject cache headers right after status line."""
        super().send_response(code, message)
        self._set_cache_headers()

    def log_message(self, fmt, *args):
        print(f"[{self.log_date_time_string()}] {args[0]} {args[1]} {args[2]}")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8001))
    server = http.server.HTTPServer(("0.0.0.0", port), CacheBustingHandler)
    print(f"Serving at http://0.0.0.0:{port} with cache-busting headers...")
    server.serve_forever()
