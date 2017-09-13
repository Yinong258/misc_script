from PIL import Image
import re

if __name__ == '__main__':
    x = 887
    y = 111
    i = 0
    j = 0

    c = Image.new("RGB", (x, y))
    file_object = open('ce.txt')

    for i in range(0, x):
        for j in range(0, y):
            line = file_object.next()
            lst = line.split(",")
            c.putpixel((i, j), (int(lst[0]), int(lst[1]), int(lst[2])))

    c.show()
    c.save("c.png")