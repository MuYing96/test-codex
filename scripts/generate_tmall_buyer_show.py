from pathlib import Path
OUT=Path('output/tmall-buyer-show'); OUT.mkdir(parents=True, exist_ok=True)
SCENES=[
('01-small-apartment-morning.svg','#e2dccd','小户型餐厅早晨，窗帘、拖鞋、纸箱和早餐杯，素人随手拍'),
('02-family-dining-evening.svg','#d6ccbc','家庭餐厅傍晚，餐桌边角、儿童水杯、购物袋，生活感'),
('03-rental-home-kitchen.svg','#e8e5da','出租屋开放厨房，冰箱贴、塑料收纳盒、围裙，不精致'),
('04-balcony-sideboard-day.svg','#dbe0d3','靠阳台餐边区，绿植、晾衣架虚影、猫抓板，真实居家'),
('05-weekend-breakfast.svg','#ece0ce','周末早餐后，面包袋、咖啡杯、厨房纸、杂物稍乱'),
('06-night-warm-light.svg','#5d5045','夜晚暖灯，外卖袋、钥匙、账单、半开的抽屉，买家秀')]

def cabinet():
 return r'''
<g id="cabinet" transform="translate(358 260)">
  <rect x="0" y="0" width="820" height="1360" fill="#1f1d19" rx="4"/>
  <rect x="70" y="45" width="680" height="210" fill="#302b26"/>
  <g><rect x="90" y="60" width="640" height="175" fill="#433c34"/><g stroke="#d6c6aa" stroke-width="2" opacity=".82">''' + ''.join(f'<line x1="{95+i*10}" y1="60" x2="{95+i*10}" y2="235"/>' for i in range(64)) + r'''</g><rect x="90" y="60" width="640" height="175" fill="url(#glass)" opacity=".45"/></g>
  <rect x="98" y="102" width="18" height="92" rx="8" fill="none" stroke="#a66f38" stroke-width="4"/><rect x="704" y="102" width="18" height="92" rx="8" fill="none" stroke="#a66f38" stroke-width="4"/>
  <rect x="70" y="280" width="680" height="150" fill="#1a1815"/><g>''' + ''.join(f'<rect x="{110+i*35}" y="320" width="24" height="72" rx="3" fill="#7830a4"/>' for i in range(9)) + ''.join(f'<rect x="{470+i*36}" y="318" width="30" height="78" fill="#eee1c8"/>' for i in range(8)) + r'''</g>
  <rect x="70" y="430" width="680" height="300" fill="#454039"/><g fill="#171614" opacity=".9">''' + ''.join(f'<ellipse cx="{110+x*35}" cy="{465+y*34}" rx="4" ry="7"/>' for x in range(18) for y in range(7)) + r'''</g><rect x="65" y="725" width="690" height="30" fill="#151411"/>
  <g><rect x="120" y="560" width="190" height="160" rx="15" fill="#e8e2d6" stroke="#8d8780" stroke-width="3"/><circle cx="153" cy="600" r="12" fill="#b7b0a8"/><circle cx="195" cy="600" r="12" fill="#b7b0a8"/><rect x="560" y="595" width="160" height="115" rx="25" fill="#eee2c7" stroke="#b0a07e" stroke-width="3"/><rect x="395" y="540" width="165" height="30" fill="#f0e6c8"/><ellipse cx="415" cy="690" rx="55" ry="18" fill="#f5eedc"/><rect x="385" y="650" width="60" height="35" fill="#f5eedc"/></g>
  <g transform="translate(0 745)"><rect x="0" y="0" width="820" height="610" fill="#1f1d19"/><rect x="30" y="35" width="370" height="95" fill="url(#wood)"/><rect x="420" y="35" width="370" height="95" fill="url(#wood)"/>
    ''' + ''.join(f'<g transform="translate(35 {150+i*140})"><rect width="360" height="115" fill="url(#wood)"/><g stroke="#6d351b" stroke-width="2">' + ''.join(f'<line x1="{25+j*14}" y1="10" x2="{25+j*14}" y2="105"/>' for j in range(23)) + '</g><circle cx="180" cy="58" r="11" fill="#b17c2b"/></g>' for i in range(3)) + r'''
    <rect x="420" y="150" width="370" height="395" fill="url(#wood)"/><rect x="455" y="190" width="140" height="325" fill="#3d3027" stroke="#663b20" stroke-width="5"/><rect x="620" y="190" width="140" height="325" fill="#3d3027" stroke="#663b20" stroke-width="5"/><g stroke="#d6c6aa" stroke-width="2" opacity=".75">''' + ''.join(f'<line x1="{460+i*10}" y1="190" x2="{460+i*10}" y2="515"/>' for i in range(30)) + r'''</g><circle cx="608" cy="365" r="10" fill="#b17c2b"/><circle cx="630" cy="365" r="10" fill="#b17c2b"/></g>
</g>'''

def scene(i,bg,desc):
 night=i==5
 extras=['<rect x="0" y="0" width="150" height="2048" fill="#f3f0e8"/><rect x="150" y="0" width="45" height="2048" fill="#bdae98"/>','<ellipse cx="350" cy="1770" rx="300" ry="190" fill="#966946"/><rect x="90" y="1590" width="590" height="55" fill="#845636"/>','<rect x="1060" y="420" width="420" height="1060" rx="10" fill="#d2d6d2"/><text x="1120" y="540" font-size="42">冰箱贴</text>','<ellipse cx="1230" cy="1330" rx="150" ry="190" fill="#5f824c"/><rect x="1208" y="1370" width="50" height="170" fill="#5a4b2d"/>','<polygon points="240,1730 430,1705 500,1850 300,1885" fill="#b97844"/>','<rect x="70" y="1470" width="210" height="140" fill="#c67b43"/><text x="95" y="1545" font-size="38">外卖袋</text>'][i]
 textcolor='#eee' if night else '#5a5048'
 return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1536" height="2048" viewBox="0 0 1536 2048">
<defs><linearGradient id="wood" x1="0" x2="1"><stop stop-color="#b9773c"/><stop offset=".5" stop-color="#d2965b"/><stop offset="1" stop-color="#8e552c"/></linearGradient><linearGradient id="glass"><stop stop-color="#fff" stop-opacity=".1"/><stop offset=".55" stop-color="#fff" stop-opacity=".38"/><stop offset="1" stop-color="#000" stop-opacity=".12"/></linearGradient><filter id="blur"><feGaussianBlur stdDeviation="18"/></filter></defs>
<rect width="1536" height="2048" fill="{bg}"/><path d="M0 1560H1536V2048H0z" fill="{'#7c5e43' if night else '#ddcaac'}"/><g stroke="{'#6f5741' if night else '#cbb99b'}" stroke-width="2" opacity=".7">{''.join(f'<line x1="{x}" y1="1560" x2="{x+520}" y2="2048"/>' for x in range(-300,1600,160))}</g><rect y="1530" width="1536" height="35" fill="{'#4d4035' if night else '#b2a694'}"/>
{extras}<ellipse cx="768" cy="1510" rx="430" ry="115" fill="#000" opacity=".22" filter="url(#blur)"/>{cabinet()}
<g font-family="Arial, sans-serif" fill="{textcolor}" opacity=".72"><text x="72" y="96" font-size="34">{desc}</text><text x="72" y="142" font-size="24">下柜90cm×宽120cm，上柜110cm×宽120cm；真实买家秀氛围</text></g>
<g opacity=".88"><rect x="250" y="1640" width="95" height="38" rx="10" fill="#e65a3c"/><rect x="980" y="1610" width="120" height="48" rx="10" fill="#f5f1e9"/><rect x="1120" y="1665" width="80" height="35" rx="8" fill="#5078aa"/><circle cx="1220" cy="1605" r="22" fill="#ead250"/></g>
</svg>'''

for i,(name,bg,desc) in enumerate(SCENES):
    (OUT/name).write_text(scene(i,bg,desc), encoding='utf-8')
(OUT/'README.md').write_text('# 天猫买家秀 6 套图\n\n本目录保留 SVG 源图；PNG 图片可通过 `python scripts/generate_tmall_buyer_show_png.py` 本地生成，但不会提交到 Git。\n\n基于用户提供的餐边柜参考制作：下柜高90公分、宽120公分，上柜高110公分、宽120公分；生成时保持黑色外框、木色抽屉/柜门、长虹玻璃、开放咖啡操作区等主要产品外观特征一致，搭配真实素人居家环境与不刻意精修的软装杂物。\n\n' + ''.join(f'- `{n}`：{d}。\n' for n,_,d in SCENES), encoding='utf-8')
