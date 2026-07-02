import re

with open('assets/js/shared-subpage-navbar.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace + text in spans with empty
content = re.sub(r'class="mobile-caret">\+</span>', 'class="mobile-caret"></span>', content)

# 2. Replace the entire cs.textContent block for caret styles
old_caret_block = r"""    cs\.textContent = \[
      '\.shared-subpage-nav \.mobile-caret, #mobile-panel-portal \.mobile-caret \{ display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px; flex: 0 0 auto; position: relative; \}',
      '\.shared-subpage-nav \.mobile-caret::before, #mobile-panel-portal \.mobile-caret::before \{ content: '\+'; font-size: 16px; font-weight: 300; color: #6e6e73; transition: transform 0\.25s ease, color 0\.2s ease; display: inline-block; line-height: 1; \}',
      '\.shared-subpage-nav \.mobile-item\.open > \.mobile-link-row \.mobile-caret::before, #mobile-panel-portal \.mobile-item\.open > \.mobile-link-row \.mobile-caret::before \{ content: '\u2212'; font-size: 16px; font-weight: 300; color: #0071e3; \}',
      'body\[data-theme="dark"\] \.shared-subpage-nav \.mobile-caret::before, body\[data-theme="dark"\] #mobile-panel-portal \.mobile-caret::before \{ color: #86868b; \}',
      'body\[data-theme="dark"\] \.shared-subpage-nav \.mobile-item\.open > \.mobile-link-row \.mobile-caret::before, body\[data-theme="dark"\] #mobile-panel-portal \.mobile-item\.open > \.mobile-link-row \.mobile-caret::before \{ color: #2997ff; \}',
    \]\.join\(''\)"""

# I need to find the actual content in the file first
# Let's find the start and end of the caret style block
start_marker = "cs.textContent = ["
end_marker = "].join('')"

start_idx = content.find(start_marker, content.find("shared-nav-caret-style"))
if start_idx < 0:
    start_idx = content.find(start_marker)
    
# Find the specific block - it's inside "shared-nav-caret-style"
cs_id_idx = content.find("shared-nav-caret-style")
block_start = content.find(start_marker, cs_id_idx)
block_end = content.find(end_marker, block_start) + len(end_marker)

old_block = content[block_start:block_end]

new_block = """    cs.textContent = [
      '.shared-subpage-nav .mobile-caret, #mobile-panel-portal .mobile-caret { display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px; flex: 0 0 auto; position: relative; }',
      '.shared-subpage-nav .mobile-caret::before, #mobile-panel-portal .mobile-caret::before { content: '+'; font-size: 16px; font-weight: 300; color: #6e6e73; transition: transform 0.25s ease, color 0.2s ease; display: inline-block; line-height: 1; }',
      '.shared-subpage-nav .mobile-item.open > .mobile-link-row .mobile-caret::before, #mobile-panel-portal .mobile-item.open > .mobile-link-row .mobile-caret::before { content: '\\u2212'; font-size: 16px; font-weight: 300; color: #0071e3; }',
      'body[data-theme="dark"] .shared-subpage-nav .mobile-caret::before, body[data-theme="dark"] #mobile-panel-portal .mobile-caret::before { color: #86868b; }',
      'body[data-theme="dark"] .shared-subpage-nav .mobile-item.open > .mobile-link-row .mobile-caret::before, body[data-theme="dark"] #mobile-panel-portal .mobile-item.open > .mobile-link-row .mobile-caret::before { color: #2997ff; }',
    ].join('')"""

content = content.replace(old_block, new_block)

with open('assets/js/shared-subpage-navbar.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Caret styles updated:")
print(f"  Old block length: {len(old_block)}")
print(f"  New block length: {len(new_block)}")

