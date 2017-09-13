#!coding:utf-8
#!/usr/bin/env python
from pwn import *
# send(data) : 发送数据
# sendline(data) : 发送一行数据，相当于在末尾加\n
# recv(numb=4096, timeout=default) : 给出接收字节数,timeout指定超时
# recvuntil(delims, drop=False) : 接收到delims的pattern
# （以下可以看作until的特例）
# recvline(keepends=True) : 接收到\n，keepends指定保留\n
# recvall() : 接收到EOF
# recvrepeat(timeout=default) : 接收到EOF或timeout
#
# interactive() : 与shell交互


 p = remote('195.154.53.62', 1337)

while (1):
    temp = p.recv()
    print temp
    temp = str(temp).split()
    a = temp[len(temp) - 4]
    b = temp[len(temp) - 2]
    c = temp[len(temp) - 3]
    num = 0

    print a+str(c)+b
    if c == '+':
        num = int(a) + int(b)
    elif c == '%':
        num = int(a) % int(b)
    elif c == '*':
        num = int(a) * int(b)
    elif c == '/':
        num = int(a) / int(b)
    elif c == '-':
        num = int(a) - int(b)
    print "num:" + str(num)
    p.send(str(num) + '\n')