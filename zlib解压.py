import zlib
import binascii
IDAT="78 9C 8B F0 75 F4 AB 0E C8 4B 8F F7 F0 4C 49 8D 2F 76 4D 2E 4A 2D A9 05 00 51 B0 07 D0 54 "
IDAT=IDAT.replace(" ","").decode('hex')
result=binascii.hexlify(zlib.decompress(IDAT))
print result.decode('hex')