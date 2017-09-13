import string
from PIL import Image
LINE=[]
x=887
y=111

c=Image.new("RGB",(x,y))

temp=open("ce.txt","r")

lines =temp.readlines()

for line in lines:
    line = line.strip('\n')
    line = line.split(',')
    LINE.append(line)
   # print LINE
print len(LINE)
print LINE[200][0]
m=0
n=0

for i in xrange(0,x):
    for j in xrange(0,y):

        c.putpixel([i,j],(int(LINE[m][0]),int(LINE[m][1]),int(LINE[m][2])))
        m +=1
        print m


c.show()