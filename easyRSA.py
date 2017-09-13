import libnum

r = open("enc.txt", "rb")
f = r.read().split()
print f
flag = ""
num=0
for c in f:
    num+=1
    n = 20473673450356553867543177537
    p = 2165121523231
    q = 9456131321351327
    e = 17
    phi = (p - 1) * (q - 1)
    d = libnum.invmod(e, phi)
    print 'd: ' + str(d)
    m = pow(int(c), d, n)
    print 'm :' + str(m)
    flag += "".join(libnum.n2s(m))
    print flag
    print num
    if '}' in flag:
        break
