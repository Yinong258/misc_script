import gmpy2



p = 23781539
q = 13574881

e = 23

phi = (p - 1)*(q - 1)
d = gmpy2.invert(e, phi)
print d

pt=gmpy2.powmod(0xdc2eeeb2782c,d,q*p)
print pt
print hex(pt)[2:].decode('hex')