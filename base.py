import base64

f=open('data.txt','rb')
content=''

for i in f.readlines():
	content+=i.strip()
while '{' not in content:
	content=base64.b64decode(content)
	
print content