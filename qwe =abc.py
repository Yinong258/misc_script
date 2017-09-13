import string

a=[]
b=[]
qwer=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
QWER=[]

print len(qwer)
for i in range(65,91):
    a.append(chr(i))
print a
for i in qwer:
#    a.append(chr(i))
    QWER.append(chr(ord(i)-32))
print QWER
#print a
#print b.index('c')


strs='f zit kggd zitkt qkt ygxk ortfzoeqs wqlatzwqss.l qfr zVg ortfzoeqs yggzwqssl Fgv oy ngx vqfz zg hxz zitd of gft soft piv dgfn lgsxzogfl qkt zitkt Zohl hstqlt eiqfut zit ygkd gy zit fxdwtk ngx utz Zit Hkgukqddtkll'
de=''
for i in strs:
    if i==' ':
        de+=' '
    elif i in string.ascii_letters:
        try:
            de+=a[qwer.index(i)]
        except:
            de+=a[QWER.index(i)]

print de