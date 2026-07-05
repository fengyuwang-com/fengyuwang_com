#!/usr/bin/env python3
import re, subprocess, pathlib

B = pathlib.Path("C:/Users/a8881/Desktop/fengyuwang_com")
r = subprocess.run(["git","ls-files"],cwd=B,capture_output=True,text=True)
files = [f.strip().strip('"') for f in r.stdout.strip().split("\n") if f.strip()]
EX = {".jpg",".jpeg",".png",".gif",".ico",".svg",".webp",".mp4",".pdf"}
results = []

# Check 1: cloudflare beacon script tag
for f in files:
    if any(f.endswith(e) for e in EX) or not f: continue
    c = open(str(B/f),"r",encoding="utf-8",errors="ignore").read()
    if "cloudflareinsights.com/beacon" in c:
        results.append((f,"CLOUDFLARE_BEACON","present"))

# Check 2: hardcoded token/secret assignments
for f in files:
    if any(f.endswith(e) for e in EX) or not f: continue
    c = open(str(B/f),"r",encoding="utf-8",errors="ignore").read()
    for m in re.finditer(r"(?i)(token|secret|apikey|api_key|credential|password)\s*[=:]\s*[\"'']?([a-zA-Z0-9_\-./+]{24,})", c):
        val = m.group(2) if m.lastindex >= 2 else m.group()
        if "tunnel" not in val.lower() and len(val) >= 16:
            results.append((f,"HARDCODED_TOKEN",val[:40]))

# Check 3: long hex strings (potential tokens)
for f in files:
    if any(f.endswith(e) for e in EX) or not f: continue
    c = open(str(B/f),"r",encoding="utf-8",errors="ignore").read()
    for m in re.finditer(r"[0-9a-f]{40}", c):
        v = m.group().lower()
        if "session" not in v and "cloudflare" not in v and v != "0"*40:
            results.append((f,"HEX40_TOKEN",m.group()))

if results:
    for r in results:
        print(r[0] + " | " + r[1] + " | " + r[2])
else:
    print("CLEAN")

