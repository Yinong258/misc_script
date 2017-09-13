import binascii,zlib,zipfile,string
ls=[]
for i in range(0,53):
	zipFile=zipfile.ZipFile('chunk'+str(i)+'.zip')
	zipInfo=zipFile.getinfo('data.txt')
	
	tmp=str(hex(zipInfo.CRC))[2:]
	if 'L' in tmp:
		tmp=tmp.replace('L','')
	ls.append(tmp)
	
print ls
def   test(real):
	for y in range(100000, 999999):
#	print i
		#print str(binascii.crc32(str(y)) & 0xffffffff)
		if real == (binascii.crc32(str(y)) & 0xffffffff):
			print(y)

ss=''


dic=[]
for a in string.letters+string.digits:
	for b in string.letters+string.digits:
		for c in string.letters+string.digits:
			for d in string.letters+string.digits:
				tmp= str(a)+str(b)+str(c)+str(d)
				dic.append(tmp)
					
for i in ls:
	real=int(i,16)
	for tmp in dic:
		if real == (binascii.crc32(tmp) & 0xffffffff):
			ss+=tmp
			print  ss
			break
						
			

	
