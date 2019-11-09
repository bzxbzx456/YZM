from random import randint

from PIL import Image,ImageDraw,ImageFont

# 测试
# 1.生成一个画布
# im = Image.new("RGB",(600,400),'red')
# im = Image.new("RGB",(600,400),(255,0,0))
# im = Image.new("RGB",(600,400),(0,255,0))
im = Image.new("RGB",(60,40),(0,0,0))

# 生成画笔
pen = ImageDraw.Draw(im)
# 画点
for i in range(500):
    pen.point((randint(1,60),randint(1,40)),'white')

# 画线
# pen.line([(0,0),(600,400)],'red',5)

# 画长方形
# pen.rectangle([(30,50),(300,200)],'yellow','pink',10)

# 画字
font = ImageFont.truetype('SIMLI.TTF',size=10,encoding='utf-8')
pen.text((10,20),"你好",font=font)
# 保存图片
im.save('1.png','PNG')