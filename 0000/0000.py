#!/usr/bin/env python
from PIL import Image,ImageDraw,ImageFont
with Image.open('./IMG_20171004_233257.jpg') as im:
    w,h=im.size
    font=ImageFont.truetype('/Library/Fonts/Arial.ttf',200)
    d=ImageDraw.Draw(im)
    d.text((4*w/5,h/5),'3',fill=(255,10,10),font=font)
    im.save('hehe.jpg')
