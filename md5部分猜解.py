import hashlib
import itertools
import hmac

key = 'c2979c7124'
dir ='1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
dir_list = itertools.product(dir, repeat=4)
for i in dir_list:
  res = hashlib.md5(''.join(i)).hexdigest()
  print i, res
  if res[0:10] == key:
    print(i)
    print(res)

print hashlib.md5('captcha')


junk='''
import hashlib
import string

strs=string.printable
ls=[]
for a in strs:
    for b in strs:
        for c in strs:
            ls.append('TASC'+a+'O3RJMV'+b+'WDJKX'+c+'ZM')
res=''
for i in ls:
    tmp=i
    i=hashlib.md5(i).hexdigest()
    #print i
    if i[:5]=='e9032':
        print i
        print tmp
        res=tmp
'''