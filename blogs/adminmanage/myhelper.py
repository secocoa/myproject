import hashlib
from PIL import Image,ImageFont,ImageDraw

from bs4 import BeautifulSoup

class Mymd5():
    def __init__(self,passwd):
        self.passwd = passwd

    def encrypt(self):
       md5 =  hashlib.md5()
       passwd = str(self.passwd) + 'holyshield'
       md5.update(passwd.encode('utf-8'))
       return  md5.hexdigest()

if __name__ == '__main__':
    mymd5 = Mymd5('199795')
    # passwd = mymd5.encrypt()
    print(mymd5.encrypt())
    print(type(mymd5.encrypt()))
    s = '''
        <font face="宋体">我们信步走进了一家乡村气息浓郁的小院子，小院里干净利落。院子中整齐地挂满了金黄的玉米，连玉米骨头都码得整整齐齐的，红红的辣椒挂在门口两侧，鸡狗猫等正悠闲地在庭院中散步，鸡屋子上有两个鸡窝， 其中一个鸡窝里正好有一枚鸡蛋，还有，绣球花等各色花儿开得正艳</font>……小院的主人已都是八十多岁高龄，男主人八十三岁，女主人八十五岁，他们还正在扒着玉米，见我们闯进院子，非但不紧张，倒是很热情，邀我们落座，还打算给我们倒热水，我们连连推辞才罢。两位老人，不紧不慢，却也一直不停歇，听他们说，现在儿孙们大都已独立，也算有出息。看到这么干净利落，充满温馨生活气息的小院，一定是老人们的生活充满追求又富有情趣，才创造了这一切的美好 。</span>
    '''
    s1 ='sdsdsdsdad'
    list1 = s1.split(',')
    for i in list1:
        print(i)
    clean_text = BeautifulSoup(s, "lxml").get_text()[:50]
    q = False
    print(clean_text)
    print(type(clean_text))
    print(int(q))