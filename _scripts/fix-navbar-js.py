#!/usr/bin/env python3
"""Fix JS syntax error in shared-subpage-navbar.js.

The CSS content property values use single quotes inside single-quoted JS strings,
which breaks JavaScript parsing. Replace with double quotes in CSS.
"""
import sys

path = r'C:\Users\a8881\Desktop\fengyuwang_com\assets\js\shared-subpage-navbar.js'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: content: '+'; -> content: "+";
old1 = (
    ".shared-subpage-nav .mobile-caret::before, "
    "#mobile-panel-portal .mobile-caret::before "
    "{ content: '+'; font-size: 16px; font-weight: 300; color: #6e6e73; "
    "transition: transform 0.25s ease, color 0.2s ease; "
    "display: inline-block; line-height: 1; }"
)
new1 = (
    ".shared-subpage-nav .mobile-caret::before, "
    "#mobile-panel-portal .mobile-caret::before "
    '{ content: "+"; font-size: 16px; font-weight: 300; color: #6e6e73; '
    "transition: transform 0.25s ease, color 0.2s ease; "
    "display: inline-block; line-height: 1; }"
)

# Fix 2: content: '\u2212'; -> content: "−";
old2 = (
    ".shared-subpage-nav .mobile-item.open > .mobile-link-row "
    ".mobile-caret::before, #mobile-panel-portal .mobile-item.open "
    "> .mobile-link-row .mobile-caret::before "
    "{ content: '\\u2212'; font-size: 16px; font-weight: 300; color: #0071e3; }"
)
new2 = (
    ".shared-subpage-nav .mobile-item.open > .mobile-link-row "
    ".mobile-caret::before, #mobile-panel-portal .mobile-item.open "
    "> .mobile-link-row .mobile-caret::before "
    '{ content: "\\u2212"; font-size: 16px; font-weight: 300; color: #0071e3; }'
)

if old1 in content:
    content = content.replace(old1, new1)
    print("Fixed line 410: content '+' using double quotes")
else:
    print("WARNING: Pattern 1 not found!")
    # Debug: show what we're looking for
    idx = content.find('mobile-caret::before')
    if idx >= 0:
        print(f"  Found near: {content[idx:idx+200]}")

if old2 in content:
    content = content.replace(old2, new2)
    print("Fixed line 411: content '\\u2212' using double quotes")
else:
    print("WARNING: Pattern 2 not found!")
    idx = content.find('mobile-item.open')
    if idx >= 0:
        print(f"  Found near: {content[idx:idx+200]}")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done - file updated")

