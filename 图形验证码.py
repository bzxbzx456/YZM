from random import randint
from PIL import Image, ImageDraw, ImageFont


# 图形验证码
class VerificationCode:
    def __init__(self, width=100, height=40, size=4):
        self.width = width
        self.height = height
        self.size = size

    def draw(self):
        im = Image.new("RGB", (self.width, self.height), self.__randcolor(150, 250))
        self.pen = ImageDraw.Draw(im)
        # 产生一个随机数字字符串
        self.code = self.__randString()
        self.__drawString()   # 画字符串
        self.__drawPoint()  # 画干扰点
        self.__drawLine()   # 画干扰线
        im.save('yzm.png')
    def __drawPoint(self):
        for i in range(500):
            self.pen.point((randint(1,self.width-1),randint(1,self.height-1)),self.__randcolor(10,80))
    def __drawLine(self):
        for i in range(5):
            x1 = randint(1,self.width-1)
            x2 = randint(1,self.width-1)
            y1 = randint(1,self.height-1)
            y2 = randint(1,self.height-1)
            self.pen.line([(x1,y1),(x2,y2)],width=1,fill=self.__randcolor(30,100))
    def __drawString(self):
        font1 = ImageFont.truetype('SIMLI.TTF', size=20, encoding='utf-8')
        for i in range(self.size):
            x = 12 + i * ((self.width - 10) // self.size)
            y = randint(5, 15)
            self.pen.text((x, y), self.code[i], font=font1, fill=self.__randcolor(50, 100))

    def __randString(self):
        res = ''
        for i in range(self.size):
            res += str(randint(0, 9))
        return res

    def __randcolor(self, low, high):
        return randint(low, high), randint(low, high), randint(low, high)


if __name__ == "__main__":
    vc = VerificationCode()
    vc.draw()
    print(vc.code)
