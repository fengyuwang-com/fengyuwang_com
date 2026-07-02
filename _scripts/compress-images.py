import os, io
from PIL import Image
exts = ('.jpg', '.jpeg', '.png')
total_old = 0
total_new = 0
for sd in ['assets/img', 'blog-pub-img']:
    if not os.path.isdir(sd): continue
    for r, d, fs in os.walk(sd):
        for f in sorted(fs):
            if not f.lower().endswith(exts): continue
            p = os.path.join(r, f)
            try:
                old = os.path.getsize(p)
                total_old += old
                img = Image.open(p)
                if f.lower().endswith(('.jpg','.jpeg')):
                    if img.mode in ('RGBA','P'): img = img.convert('RGB')
                    best, bbuf = old, None
                    for q in [80,75,70,65]:
                        b = io.BytesIO()
                        img.save(b, format='JPEG', optimize=True, quality=q)
                        if b.tell() < best:
                            best, bbuf = b.tell(), b
                else:
                    b = io.BytesIO()
                    img.save(b, format='PNG', optimize=True, compress_level=9)
                    best, bbuf = b.tell(), b
                total_new += best
                if best < old and bbuf:
                    bbuf.seek(0)
                    with open(p, 'wb') as fout:
                        fout.write(bbuf.read())
                pct = (1 - best/old) * 100
                print(f'{f:40s} {old/1024:>7.1f}KB -> {best/1024:>7.1f}KB ({pct:>5.0f}%)')
            except Exception as e:
                print(f'{f:40s} SKIP ({e})')
print(f'Total: {total_old/1024:.0f}KB -> {total_new/1024:.0f}KB')
