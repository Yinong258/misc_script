from bs4 import BeautifulSoup
import requests
import re

ok=requests.session()
url='http://web.sycsec.com/0b3a7c6ca7f1f2e6/'

temp = ok.get(url)
soup=BeautifulSoup(temp.content)

ss=str(soup)
times= soup.text.count('@')

times= times-1
print times
datas={'mytext':times}
print datas



a=ok.post('http://web.sycsec.com/0b3a7c6ca7f1f2e6/judge.php',data=datas)
print a.text

