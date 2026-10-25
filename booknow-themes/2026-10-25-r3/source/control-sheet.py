from pathlib import Path
from PIL import Image,ImageOps,ImageDraw,ImageFont,ImageFilter
import json
root=Path(__file__).resolve().parent.parent
brands=json.loads((root/'source/brands.json').read_text());font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',20);small=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',15)
sheet=Image.new('RGB',(1440,1470),'#f0f1e8');d=ImageDraw.Draw(sheet)
d.text((24,20),'R3 / five image-control systems / actual extracted-ZIP CSS',font=font,fill='#20291f')
headers=['Native home / colour','Native gallery / colour','Native home / monochrome','Native gallery / monochrome']
for i,t in enumerate(headers):d.text((100+i*330,70),t,font=small,fill='#20291f')
for row,b in enumerate(brands):
 y=110+row*250;d.text((24,y+90),chr(65+row),font=font,fill='#20291f')
 for col in range(4):
  im=Image.open(root/'previews'/b['id']/('controls-detail-home.png' if col%2==0 else 'controls-detail-native-gallery.png')).convert('RGB')
  if col>=2:im=ImageOps.grayscale(im).convert('RGB')
  # No upscaling: preserve the rendered detail and relative target geometry.
  if im.width>300 or im.height>220:im.thumbnail((300,220))
  x=100+330*col;sheet.paste(im,(x+(300-im.width)//2,y+(220-im.height)//2))
 d.line((24,y+235,1410,y+235),fill='#b9c1ae')
for i,b in enumerate(brands):d.text((24,1385+i*16),chr(65+i)+'  '+b['name'],font=small,fill='#20291f')
sheet.save(root/'previews/image-controls-comparison.png')
states=Image.new('RGB',(1100,460),'#f0f1e8');dd=ImageDraw.Draw(states);dd.text((20,14),'R3 / photo controls: normal, hover, focus-visible, pointer-pressed',font=font,fill='#20291f')
for i,b in enumerate(brands):
 x=20+i*215;dd.text((x,60),b['id'],font=small,fill='#20291f')
 for j,name in enumerate(['normal','hover','focus','pressed']):
  im=Image.open(root/'previews'/b['id']/('control-'+name+'.png')).convert('RGB');states.paste(im,(x,100+j*80));dd.text((x+90,115+j*80),name,font=small,fill='#20291f')
dd.text((20,435),'Focus shown on authored keyboard fixture; native IMG keyboard semantics require vendor support.',font=small,fill='#20291f');states.save(root/'previews/control-states.png')
print('Colour/monochrome home+dialog comparison and control-state sheet saved.')
