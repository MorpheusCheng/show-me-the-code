#!/usr/bin/env python
import requests,re,os
def savePageInfo(url,position,regx):
    html=requests.get(url).text
    pic_url=re.findall(regx,html)

    i=0
    for each in pic_url:
        pic = requests.get(each)
        print(each)
        if not os.path.isdir(position):
            os.mkdir(position)
        fp=open(position+'/'+str(i)+'.jpg','wb')
        fp.write(pic.content)
        fp.close()
        i=i+1



url='http://tieba.baidu.com/p/2166231880'
position='./picture'
regx=r'src="(http://imgsrc.baidu.com/forum/.*?)"'

if __name__ == '__main__':
    savePageInfo(url,position,regx)

