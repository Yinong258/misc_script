#coding=utf-8
import re
import requests
url='http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1469523304984_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%90%9E%E7%AC%91%E5%8A%A8%E5%9B%BE'

a=requests.get(url).content
pic_url = re.findall('"objurl":"(.*?)",',a,re.I)
i =0
print pic_url
for each in pic_url:
    #print each
    try:
        pic =requests.get(each,timeout=1)
    except requests.exceptions.ConnectionError:
        print 'ERROR'
        continue
    string ='pictures'+str(i) + '.gif'
    fp =open(string,'wb')
    #fp.write(pic.content)
    fp.close()
    i+=1
