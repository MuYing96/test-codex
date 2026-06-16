"""Generate six dependency-free PNG buyer-show scene previews.

The environment does not provide raster imaging libraries, so this script writes
PNG files directly with zlib-compressed RGB scanlines and draws simple lifestyle
scenes using primitive shapes. It mirrors the SVG scene set and keeps the same
cabinet visual constants: black frame, wood drawer/door faces, fluted glass,
open coffee station, and a 120cm-wide / 90cm+110cm-high proportion cue.
"""
from pathlib import Path
import math, struct, zlib, random

W, H = 900, 1200
OUT = Path('output/tmall-buyer-show')
OUT.mkdir(parents=True, exist_ok=True)
SCENES = [
    ('01-small-apartment-morning.png', (226, 220, 205), '小户型餐厅早晨'),
    ('02-family-dining-evening.png', (214, 204, 188), '家庭餐厅傍晚'),
    ('03-rental-home-kitchen.png', (232, 229, 218), '出租屋开放厨房'),
    ('04-balcony-sideboard-day.png', (219, 224, 211), '靠阳台餐边区'),
    ('05-weekend-breakfast.png', (236, 224, 206), '周末早餐后'),
    ('06-night-warm-light.png', (93, 80, 69), '夜晚暖灯'),
]

def rgb(hexstr):
    hexstr = hexstr.lstrip('#')
    return tuple(int(hexstr[i:i+2], 16) for i in (0, 2, 4))

class Canvas:
    def __init__(self, w, h, bg):
        self.w, self.h = w, h
        self.p = bytearray(bg * (w*h))
    def px(self, x, y, c):
        if 0 <= x < self.w and 0 <= y < self.h:
            i = (y*self.w + x)*3; self.p[i:i+3] = bytes(c)
    def rect(self, x1, y1, x2, y2, c):
        x1=max(0,int(x1)); y1=max(0,int(y1)); x2=min(self.w,int(x2)); y2=min(self.h,int(y2))
        row = bytes(c) * max(0, x2-x1)
        for y in range(y1, y2):
            i=(y*self.w+x1)*3; self.p[i:i+len(row)] = row
    def ellipse(self, cx, cy, rx, ry, c):
        for y in range(max(0,int(cy-ry)), min(self.h,int(cy+ry)+1)):
            dy=(y-cy)/ry
            span=int(rx*math.sqrt(max(0,1-dy*dy)))
            self.rect(cx-span, y, cx+span, y+1, c)
    def line(self, x1, y1, x2, y2, c, width=1):
        steps=max(abs(int(x2-x1)), abs(int(y2-y1)), 1)
        for s in range(steps+1):
            t=s/steps; x=int(x1+(x2-x1)*t); y=int(y1+(y2-y1)*t)
            self.rect(x-width//2, y-width//2, x+width//2+1, y+width//2+1, c)
    def poly(self, pts, c):
        miny=max(0,min(y for _,y in pts)); maxy=min(self.h-1,max(y for _,y in pts))
        for y in range(int(miny), int(maxy)+1):
            xs=[]
            for (x1,y1),(x2,y2) in zip(pts, pts[1:]+pts[:1]):
                if (y1<=y<y2) or (y2<=y<y1):
                    xs.append(x1+(y-y1)*(x2-x1)/(y2-y1))
            xs.sort()
            for a,b in zip(xs[0::2], xs[1::2]): self.rect(a,y,b,y+1,c)
    def wood(self, x1, y1, x2, y2, base, seed):
        rnd=random.Random(seed); self.rect(x1,y1,x2,y2,base)
        for y in range(y1,y2,6):
            d=rnd.randint(-18,18); col=tuple(max(0,min(255,v+d)) for v in base)
            self.line(x1,y,x2,y+rnd.randint(-1,1),col,1)
    def png(self, path):
        raw = bytearray()
        stride = self.w*3
        for y in range(self.h):
            raw.append(0); raw.extend(self.p[y*stride:(y+1)*stride])
        def chunk(tag, data):
            return struct.pack('>I', len(data))+tag+data+struct.pack('>I', zlib.crc32(tag+data)&0xffffffff)
        data = b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', self.w,self.h,8,2,0,0,0)) + chunk(b'IDAT', zlib.compress(bytes(raw), 9)) + chunk(b'IEND', b'')
        Path(path).write_bytes(data)

def fluted(c, x1, y1, x2, y2):
    c.rect(x1,y1,x2,y2,rgb('#453c32'))
    for x in range(x1,x2,6):
        c.line(x,y1,x,y2,rgb('#d8c9ad'),1); c.line(x+2,y1,x+2,y2,rgb('#594d42'),1)

def cabinet(c, seed=0):
    x, y, cw = 210, 170, 480
    upper, lower = 435, 355
    black=rgb('#1f1d19')
    c.rect(x,y,x+cw,y+upper+lower,black)
    c.rect(x+40,y+25,x+cw-40,y+145,rgb('#302b26')); fluted(c,x+52,y+34,x+cw-52,y+136)
    c.rect(x+55,y+60,x+66,y+112,rgb('#a66f38')); c.rect(x+cw-66,y+60,x+cw-55,y+112,rgb('#a66f38'))
    c.rect(x+40,y+160,x+cw-40,y+250,rgb('#1a1815'))
    for i in range(7): c.rect(x+62+i*22,y+184,x+77+i*22,y+226,rgb('#7830a4'))
    for i in range(6): c.rect(x+285+i*22,y+184,x+303+i*22,y+228,rgb('#eee1c8'))
    c.rect(x+40,y+250,x+cw-40,y+430,rgb('#454039'))
    for px in range(x+65,x+cw-60,20):
        for py in range(y+270,y+405,20): c.ellipse(px,py,2,4,rgb('#171614'))
    c.rect(x+70,y+330,x+180,y+420,rgb('#e8e2d6')); c.ellipse(x+90,y+354,7,7,rgb('#b7b0a8'))
    c.rect(x+325,y+352,x+420,y+418,rgb('#eee2c7')); c.ellipse(x+245,y+408,34,10,rgb('#f5eedc'))
    ly=y+upper
    c.rect(x,ly,x+cw,ly+lower,black)
    c.wood(x+18,ly+22,x+235,ly+78,rgb('#be7c41'),seed+1); c.wood(x+247,ly+22,x+462,ly+78,rgb('#be7c41'),seed+2)
    for j in range(3):
        yy=ly+90+j*82; c.wood(x+20,yy,x+232,yy+65,rgb('#b9773c'),seed+3+j)
        for xx in range(x+35,x+220,8): c.line(xx,yy+6,xx,yy+59,rgb('#6d351b'),1)
        c.ellipse(x+126,yy+32,6,6,rgb('#b17c2b'))
    c.wood(x+247,ly+90,x+462,ly+312,rgb('#b9773c'),seed+9)
    fluted(c,x+270,ly+112,x+350,ly+295); fluted(c,x+365,ly+112,x+445,ly+295)
    c.ellipse(x+352,ly+205,6,6,rgb('#b17c2b')); c.ellipse(x+365,ly+205,6,6,rgb('#b17c2b'))

def scene(idx, bg):
    c=Canvas(W,H,bg); night=idx==5
    floor=rgb('#7c5e43') if night else rgb('#ddcaac')
    base=rgb('#4d4035') if night else rgb('#b2a694')
    c.rect(0,880,W,H,floor); c.rect(0,862,W,884,base)
    grid=rgb('#6f5741') if night else rgb('#cbb99b')
    for x in range(-200,W,95): c.line(x,880,x+310,H,grid,1)
    if idx in (0,3): c.rect(0,0,90,H,rgb('#f3f0e8')); c.rect(90,0,116,H,rgb('#bdae98'))
    if idx==1: c.ellipse(205,1040,180,90,rgb('#966946')); c.rect(55,955,400,990,rgb('#845636'))
    if idx==2: c.rect(640,250,875,858,rgb('#d2d6d2')); [c.rect(665+i*24,310+i*31,700+i*24,326+i*31,(190-i*12,110+i*10,120+i*8)) for i in range(6)]
    if idx==3: c.ellipse(720,760,85,120,rgb('#5f824c')); c.rect(705,805,735,890,rgb('#5a4b2d'))
    if idx==4: c.poly([(140,1015),(260,1000),(305,1085),(175,1105)], rgb('#b97844'))
    if idx==5: c.rect(45,860,175,935,rgb('#c67b43'))
    c.ellipse(450,870,260,60,(0,0,0)); cabinet(c,idx*10)
    # casual clutter
    for n,col in enumerate([rgb('#e65a3c'),rgb('#f5f1e9'),rgb('#5078aa'),rgb('#ead250')]):
        c.rect(130+n*165,965+(n%2)*35,190+n*165,990+(n%2)*35,col)
    return c

for idx,(name,bg,_desc) in enumerate(SCENES):
    scene(idx,bg).png(OUT/name)
print('wrote', len(SCENES), 'png files to', OUT)
