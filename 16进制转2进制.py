with open('233.txt', 'r') as f:
	data = f.read()
with open('233', 'wb') as f:
	f.write(binascii.unhexlify(data.strip()))