__author__ = 'Adam'
class MyError(Exception):
      pass

class DesWrongLenght(MyError):
    """Wrong length of key, it should be multiple of 8 bytes"""

