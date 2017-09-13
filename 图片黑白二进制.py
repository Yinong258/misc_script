from PIL import Image

flag = ''
flag1 = ''
for i in range(304):
	pot = "test-{0}.png".format(i)
	im = Image.open(pot)
	s = im.getpixel((0,0))
	if s == 255:
		flag += '0'
		flag1 += '1'
	else:
		flag += '1'
		flag1 += '0'

print 'flag:',flag 
print 'flag1:',flag1