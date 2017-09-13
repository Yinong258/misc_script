# encoding:utf-8
import base64
from Crypto.Cipher import AES
from Crypto import Random
 
def encrypt(data, password):
    bs = AES.block_size
    pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    iv = Random.new().read(bs)
    cipher = AES.new(password, AES.MODE_CBC, iv)
    data = cipher.encrypt(pad(data))
    data = iv + data
    return data
 
def decrypt(data, password):
    bs = AES.block_size
    if len(data) <= bs:
        return data
    unpad = lambda s : s[0:-ord(s[-1])]
    iv = data[:bs]
    cipher = AES.new(password, AES.MODE_CBC, iv)
    data  = unpad(cipher.decrypt(data[bs:]))
    return data
 
if __name__ == '__main__':
    data = ' c086e08ad8ee0ebe7c2320099cfec9eea9a346a108570a4f6494cfe7c2a30ee1'
    password = '0a0e176722a95a623f47fa17f02cc16a' #16,24,32位长的密码
    encrypt_data = encrypt(data, password)
    encrypt_data = base64.b64encode(encrypt_data)
    print 'encrypt_data:', encrypt_data
 
 
    encrypt_data = base64.b64decode(encrypt_data)
    decrypt_data = decrypt(encrypt_data, password)
    print 'decrypt_data:', decrypt_data
