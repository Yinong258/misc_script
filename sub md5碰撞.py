import hashlib
cap=raw_input()
for i in range(0,100000):
	res=hashlib.md5(str(i)).hexdigest()
	if cap== res[:4]:
		print str(i)