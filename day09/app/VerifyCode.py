import os
from io import BytesIO
from random import randint

from PIL import ImageFont,Image,ImageDraw

from day09 import settings


class VerifyCode():
    def __init__(self,width=100,height=40,len=4):
        '''
        :param width:  #验证码图片宽度
        :param height: #验证码图片高度
        :param len:  #验证码长度
        '''
        self.width  = width if width > 50 else 100
        self.height = height if height > 30 else 40
        self.len = len if len >= 4 else 4
        self._code = '' #验证码字符串
        self.__pen = None #画笔

    def output(self):
        '''
        输出验证码
        :return:返回验证码图片的二进制流
        '''
        # 1 创建画布
        im = Image.new('RGB',(self.width,self.height),self.__randColor(120,200))
        self.__pen = ImageDraw.Draw(im) #产生画笔
        # 2 产生验证码
        self.generate_code()
        # 3.画验证码
        self.__drawCode()
        # 4.画点
        self.__drawPoint()
        # 5.画线
        self.__drawLine()
        #6 保存图片
        #im.save('vc.png','PNG')
        buf = BytesIO()
        im.save(buf, 'png')
        res = buf.getvalue()
        buf.close()
        return res


    def __randColor(self,low,hight):
        '''

        :return: 返回随机颜色
        '''
        return randint(low,hight),randint(low,hight),randint(low,hight)

    def generate_code(self):
        '''
        产生纯数字验证码字符串
        :return: 数字验证码字符串
        '''
        num = ''
        for i in range(self.len):
            num += str(randint(0,9))
        self._code = num

    def __drawCode(self):
        '''
        画验证码
        :return:
        '''
        #path = os.path.join(settings.STATICFILES_DIRS[0],'font/SIMFANG.TTF')
        path = os.path.join(settings.STATICFILES_DIRS[0],'font/SIMFANG.TTF')
        print(path)
        font1 = ImageFont.truetype(path,size=20,encoding='utf-8')
        # 一个字符的宽度
        width = (self.width - 20) / self.len

        for i in range(self.len):
            x = 10 + i * width
            y = randint(5, self.height - 15)
            self.__pen.text((x, y), self._code[i], font=font1, fill=self.__randColor(0, 100))


    def __drawPoint(self):
        for i in range(300):
            x = randint(0,self.width-1)
            y = randint(0,self.height-1)

            self.__pen.point((x,y),fill=self.__randColor(60,160))

    def __drawLine(self):
        for i in range(6):
            startloction =(randint(0,self.width-1),randint(0,self.height-1))
            endloction = (randint(0,self.width-1),randint(0,self.height-1))
            self.__pen.line([startloction,endloction],fill=self.__randColor(20,130))

if __name__ == '__main__':
    vc = VerifyCode()
    vc.output()
