from MyError import DesWrongLenght

__author__ = 'Adam'
from Crypto.Cipher import DES,DES3,AES,XOR
import MyError
import ctypes


from Crypto import Random

def Des_Encrypt(mode,input,key,iv):
    try:
        if len(input) %16 != 0:
            raise DesWrongLenght("wrong length of input. Should be multiple of 8 bytes")
        if len(key) !=16:
            raise DesWrongLenght("wrong length of key should be 8 bytes")

        if mode=="ECB":
            des = DES.new(key.decode('hex'), DES.MODE_ECB)
            ciph=des.encrypt(input.decode('hex'))
            return ciph
        if mode=="CBC":
            des=DES.new(key.decode('hex'), DES.MODE_CBC,iv.decode('hex'))
            ciph=des.encrypt(input.decode('hex'))
            return ciph
    except DesWrongLenght as exc:
        ctypes.windll.user32.MessageBoxW(0,unicode(exc),u"Error",0)

def Des_Decrypt(mode,input,key,iv):
    try:
        if len(input) %16 != 0:
            raise DesWrongLenght("wrong length of input. Should be multiple of 8 bytes")
        if len(key) !=16:
            raise DesWrongLenght("wrong length of key should be 8 bytes")
        if mode=="ECB":
            des = DES.new(key.decode('hex'), DES.MODE_ECB)
            ciph=des.decrypt(input.decode('hex'))
            return ciph.rstrip('0')
        if mode=="CBC":
            des=DES.new(key.decode('hex'), DES.MODE_CBC,iv.decode('hex'))
            ciph=des.decrypt(input.decode('hex'))
            return ciph.rstrip('0')
    except DesWrongLenght as exc:
        ctypes.windll.user32.MessageBoxW(0,unicode(exc),u"Error",0)


def compute_KCV(key):
    try:
        if len(key)==16:
            des = DES.new(key.decode('hex'), DES.MODE_ECB)
            ciph = des.encrypt('00000000000000000000000000000000'.decode('hex'))
            return ciph
        elif len (key)==32:
            des = DES3.new(key.decode('hex'), DES3.MODE_ECB)
            ciph = des.encrypt('00000000000000000000000000000000'.decode('hex'))
            return ciph
        else:
            raise DesWrongLenght("Key can have length of 16 or 32 bytes")
    except DesWrongLenght as exc:
        ctypes.windll.user32.MessageBoxW(0,unicode(exc),u"Error",0)

def triple_Des_encrypt(mode,input,key,iv):
    try:
        if len(input) %16 != 0:
            raise DesWrongLenght("wrong length of input. Should be multiple of 8 bytes")
        if len(key) !=32:
            raise DesWrongLenght("wrong length of key should be 16 bytes")
        if mode=="ECB":
            des = DES3.new(key.decode('hex'), DES.MODE_ECB)
            ciph=des.encrypt(input.decode('hex'))
            return ciph
        if mode=="CBC":
            des=DES3.new(key.decode('hex'), DES.MODE_CBC,iv.decode('hex'))
            ciph=des.encrypt(input.decode('hex'))
            return ciph
    except DesWrongLenght as exc:
        ctypes.windll.user32.MessageBoxW(0,unicode(exc),u"Error",0)

def triple_Des_Decrypt(mode,input,key,iv):
    try:
        if len(input) %16 != 0:
            raise DesWrongLenght("wrong length of input. Should be multiple of 8 bytes")
        if len(key) !=32:
            raise DesWrongLenght("wrong length of key should be 16 bytes")
        if mode=="ECB":
            des = DES3.new(key.decode('hex'), DES.MODE_ECB)
            ciph=des.decrypt(input.decode('hex'))
            return ciph
        if mode=="CBC":
            des=DES3.new(key.decode('hex'), DES.MODE_CBC,iv)
            ciph=des.decrypt(input.decode('hex'))
            return ciph
    except DesWrongLenght as exc:
        ctypes.windll.user32.MessageBoxW(0,unicode(exc),u"Error",0)

def AES_encryption(mode,input,key):
    try:
        if len(input) % 32!=0:
            raise DesWrongLenght("Input should be multiple of 16 bytes long")
        if len(key) !=32 and len(key)!=48 and len(key)!=64 :
            raise DesWrongLenght("wrong length of key should be 16, 24 or 32 bytes long")
        if mode== "CBC":
            iv = "00000000000000000000000000000000".decode('hex')
            cipher = AES.new( key.decode('hex'), AES.MODE_CBC, iv )
            return cipher.encrypt(input.decode('hex') )
        if mode== "ECB":
            cipher = AES.new( key.decode('hex'), AES.MODE_ECB)
            return cipher.encrypt(input.decode('hex') )
    except DesWrongLenght as exc:
        ctypes.windll.user32.MessageBoxW(0,unicode(exc),u"Error",0)

def AES_decryption(mode,input,key):
    try:
        if len(input) % 32!=0:
            raise DesWrongLenght("Input should be multiple of 16 bytes long")
        if len(key) !=32 and len(key)!=48 and len(key)!=64 :
            raise DesWrongLenght("wrong length of key should be 16, 24 or 32 bytes long")
        if mode== "CBC":
            iv = "00000000000000000000000000000000".decode('hex')
            cipher = AES.new( key.decode('hex'), AES.MODE_CBC, iv )
            return cipher.decrypt(input.decode('hex') )
        if mode== "ECB":
            cipher = AES.new( key.decode('hex'), AES.MODE_ECB)
            return cipher.decrypt(input.decode('hex') )
    except DesWrongLenght as exc:
        ctypes.windll.user32.MessageBoxW(0,unicode(exc),u"Error",0)
def xor_calc(input,input2):
    try:
        if len(input) % 2 !=0 or len(input2) % 2 != 0:
            raise DesWrongLenght("Input fields must have even length")
        cipher = XOR.new(input2.decode('hex'))
        return cipher.encrypt(input.decode('hex'))
    except DesWrongLenght as exc:
        ctypes.windll.user32.MessageBoxW(0,unicode(exc),u"Error",0)
