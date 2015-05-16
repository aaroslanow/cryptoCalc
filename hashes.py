__author__ = 'Adam'


from Crypto.Hash import SHA as SHA1

def getSHA1_Text(input):
    result = SHA1.new()
    result.update(input)
    return result.hexdigest()

def getSHA1_File(file_path):

    file_content = open(file_path)
    file_content= file_content.read()
    return getSHA1_Text(file_content)
