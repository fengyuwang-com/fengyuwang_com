#!/usr/bin/env python3
"""Remove the Jensen Huang easter egg from AI and Cloud pages.
Keep it only on portfolio (tech) pages.
"""
import sys

files = [
    'en/ai.html', 'en/cloud.html',
    'zh-cn/ai.html', 'zh-cn/cloud.html',
    'zh-hk/ai.html', 'zh-hk/cloud.html',
]

for f in files:
    path = 'C:/Users/a8881/Desktop/fengyuwang_com/' + f
    with open(path, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    # Find the easter egg: <div style="text-align:center; padding:60px 20px 40px;">
    # containing With Huang.jpg
    # We remove up to the next </div> that follows
    
    marker = 'With Huang.jpg'
    pos = content.find(marker)
    if pos == -1:
        print(f + ': No easter egg found')
        continue
    
    # Find the opening <div that contains style="text-align:center; padding:60px 20px 40px;"
    # or similar - search backwards from marker
    div_start = content.rfind('<div', 0, pos)
    if div_start == -1:
        print(f + ': Could not find opening div')
        continue
    
    # Find the closing </div> after the marker
    div_end = content.find('</div>', pos)
    if div_end == -1:
        print(f + ': Could not find closing div')
        continue
    
    div_end += len('</div>')  # include the closing tag
    
    # Verify we're removing the right thing
    removed = content[div_start:div_end]
    if 'With Huang' not in removed and '黄仁勋' not in removed:
        print(f + ': Unexpected content, skipping: ' + removed[:80])
        continue
    
    # Build new content
    new_content = content[:div_start] + content[div_end:]
    
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(new_content)
    
    print(f + ': Removed easter egg (' + str(len(removed)) + ' chars)')

print('Done')

