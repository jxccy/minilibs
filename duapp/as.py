#
# Python2

import base64
from Crypto.Cipher import AES
from hashlib import md5

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

class AESCipher:

    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        raw = pad(raw)
        # iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_ECB)
        return base64.b64encode(cipher.encrypt( raw ) )


cipher = AESCipher('b46afc89e13025d7')
encrypted = cipher.encrypt('isChest0loginTokenc3617d9b|71354952|9a792158aa7b730dplatformandroidproductId39628timestamp1566206310786uuid47e122719530a8fbv4.9.0')
print(md5(encrypted.encode('utf-8')).hexdigest())