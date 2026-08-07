#!/usr/bin/env node
/**
 * apply-mobile-fix.js
 *
 * Global rollout of two mobile/CTA fixes across the trilingual content pages
 * (en/, zh-cn/, zh-hk/), mirroring what was piloted on zh-cn/tech.html:
 *
 *  Fix A — mobile text width: shrink nested card horizontal padding inside
 *          each page's `@media (max-width: 599px)` block so text lines widen.
 *          .block-inner       0 24px -> 0 12px
 *          .section-card      32px   -> 20px
 *          .content-text-card 0 24px -> 0 16px
 *  Fix B — CTA buttons equal width inside `.cta-row` (align to longest, capped).
 *
 * CSS is inline per-page, in two whitespace variants (minified single-line and
 * spaced multi/single-line). Both share ONE unique anchor per file: the
 * `.block-inner h2 { font-size: 1.25rem; }` rule, which sits at the tail of the
 * 599px block in every content sub-page (verified: exactly one occurrence).
 *
 * Idempotent: skips a file when Fix A tokens are already present.
 * Only writes files that actually change. Prints a per-file {status} line.
 *
 * Usage: node scripts/apply-mobile-fix.js   (run from repo root)
 */
"use strict";
const fs = require("fs");
const path = require("path");

const ROOT = path.join(__dirname, "..");
const DIRS = ["en", "zh-cn", "zh-hk"];

// ---- Fix A rules ----
const MIN_RULES =
  ".block-inner{padding-left:12px;padding-right:12px}" +
  ".section-card{padding:20px}" +
  ".content-text-card{padding-left:16px;padding-right:16px}";

const SPACED_RULES = [
  ".block-inner { padding-left: 12px; padding-right: 12px; }",
  ".section-card { padding: 20px; }",
  ".content-text-card { padding-left: 16px; padding-right: 16px; }",
];

// Fix B replacement for the cta-row button rule.
const CTA_REPLACE =
  ".cta-row .default-btn, .cta-row .default-btn-one { flex: 1 1 auto; min-width: 160px; max-width: 240px; text-align: center; }";

let changed = [];
let skipped = [];
let ctaFixed = 0;

for (const dir of DIRS) {
  const fullDir = path.join(ROOT, dir);
  for (const name of fs.readdirSync(fullDir)) {
    if (!name.endsWith(".html")) continue;
    const file = path.join(fullDir, name);
    let s = fs.readFileSync(file, "utf8");
    const orig = s;
    let minified = false;

    // ================= Fix A =================
    const hasFixA =
      s.includes(".content-text-card{padding-left:16px") ||
      s.includes(".content-text-card { padding-left: 16px");
    if (hasFixA) {
      skipped.push(dir + "/" + name + " (already has Fix A)");
    } else {
      const anchorIdx = s.indexOf("1.25rem");
      const hasTextCard = s.includes(".content-text-card");
      if (anchorIdx === -1 && !hasTextCard) {
        // No 599 anchor and no text cards at all — nothing to fix here.
        skipped.push(dir + "/" + name + " (no 599 anchor, no text cards)");
      } else if (anchorIdx === -1 && hasTextCard) {
        // Truncated media block: has content-text-card but the 599px block is
        // missing the `.block-inner h2 ... 1.25rem` rule. Fall back to inserting
        // the minified rules right after the opening brace of the 599px block.
        const media599 = "@media(max-width:599px){";
        const mIdx = s.indexOf(media599);
        if (mIdx !== -1) {
          const openIdx = mIdx + media599.length;
          s = s.slice(0, openIdx) + MIN_RULES + s.slice(openIdx);
          minified = true;
        } else {
          const media599s = "@media (max-width: 599px) {";
          const ms = s.indexOf(media599s);
          if (ms !== -1) {
            const openIdx = ms + media599s.length;
            const inline = " " + SPACED_RULES.join(" ") + " ";
            s = s.slice(0, openIdx) + inline + s.slice(openIdx);
          } else {
            skipped.push(dir + "/" + name + " (no 599 block at all)");
          }
        }
      } else {
        // Standard path: 1.25rem anchor exists.
        const selBegin = s.lastIndexOf(".block-inner h2", anchorIdx);
        minified = s[selBegin + ".block-inner h2".length] === "{";

        if (minified) {
          const ruleClose = s.indexOf("}", anchorIdx);
          s = s.slice(0, ruleClose + 1) + MIN_RULES + s.slice(ruleClose + 1);
        } else {
          const onOwnLine = /\n[ \t]*$/.test(s.slice(0, selBegin));
          if (onOwnLine) {
            const lineStart = s.lastIndexOf("\n", selBegin) + 1;
            const lead = (s.slice(lineStart, selBegin).match(/^[ \t]*/) || [""])[0];
            const block = SPACED_RULES.map((r) => lead + r).join("\n");
            s = s.slice(0, lineStart) + block + "\n" + s.slice(lineStart);
          } else {
            const inline = " " + SPACED_RULES.join(" ") + " ";
            s = s.slice(0, selBegin) + inline + s.slice(selBegin);
          }
        }
      }
    }

    // ================= Fix B =================
    if (s.includes(".cta-row .default-btn")) {
      const selStart = s.indexOf(".cta-row .default-btn");
      const taIdx = s.indexOf("text-align", selStart);
      const closeIdx = s.indexOf("}", taIdx);
      if (selStart !== -1 && taIdx !== -1 && closeIdx !== -1) {
        s = s.slice(0, selStart) + CTA_REPLACE + s.slice(closeIdx + 1);
        ctaFixed++;
      }
    }

    if (s !== orig) {
      fs.writeFileSync(file, s, "utf8");
      changed.push(dir + "/" + name + (minified ? " [minified]" : ""));
    }
  }
}

console.log("=== Fix A/B applied (changed) ===");
console.log(changed.join("\n") || "(none)");
console.log("\nChanged files:", changed.length);
console.log("Fix B (cta buttons) fixed:", ctaFixed);
console.log("\nSkipped:", skipped.length);
if (skipped.length) console.log(skipped.join("\n"));
