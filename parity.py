from MyError import DesWrongLenght

__author__ = 'Adam'
import MyError
import ctypes
def check_parity(input):
    try:
        if len(input) % 2 != 0:
            raise DesWrongLenght("Length of input should be even")
        a=[]
        input = input.zfill(len(input) + len(input) % 2)  # pad with zeros for even digits

        for i in range(0, len(input), 2):  # split into 2-digit chunks
            splitted_text = ''.join(input[i: i+2])
            binres= bin(int(splitted_text,16))[2:].zfill(8)
            positives = binres.count('1')
            if positives % 2 ==1:
                a.append("true")
            elif positives % 2 ==0:
                a.append("false")

        if len(a)==a.count("true"):
            return "Key is odd parity"
        elif len(a)==a.count("false"):
            return "Key is even parity"
        else:
            return "NO PARITY!"
    except DesWrongLenght as exc:
            ctypes.windll.user32.MessageBoxW(0,unicode(exc),u"Error",0)

def compute_parity(mode, input):
    try:
        if len(input) % 2 != 0:
            raise DesWrongLenght("Length of input should be even")
        input = input.zfill(len(input) + len(input) % 2)  # pad with zeros for even digits
        result =""
        if mode== "Odd parity":
            for i in range(0, len(input), 2):  # split into 2-digit chunks
                splitted_text = ''.join(input[i: i+2])
                binres= bin(int(splitted_text,16))[2:].zfill(8)
                positives = binres.count('1')
                if positives % 2 ==1:
                    result +=hex(int(binres,2))[2:]
                elif positives % 2 ==0:
                    if str(binres)[7:]=='1':
                        result+=hex(int(binres,2)-1)[2:]
                    if str(binres)[7:]=='0':
                        result+=hex(int(binres,2)-1)[2:]
            return result.upper()

        if mode== "Even parity":
            for i in range(0, len(input), 2):  # split into 2-digit chunks
                splitted_text = ''.join(input[i: i+2])
                binres= bin(int(splitted_text,16))[2:].zfill(8)
                positives = binres.count('1')
                if positives % 2 ==0:
                    result +=hex(int(binres,2))[2:]
                elif positives % 2 ==1:
                    if str(binres)[7:]=='1':
                        result+=hex(int(binres,2)-1)[2:]
                    if str(binres)[7:]=='0':
                        result+=hex(int(binres,2)-1)[2:]
            return result.upper()
    except DesWrongLenght as exc:
            ctypes.windll.user32.MessageBoxW(0,unicode(exc),u"Error",0)