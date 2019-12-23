from PIL import Image
import pytesseract
import os, sys
from aip import AipOcr



# get the image and convert to the string. 
def convert(file_name, client_account):    
    with open(file_name, 'rb') as fp:
        image = fp.read()
    msg = client_account.basicGeneral(image)   # 解析图片
    text = msg.get('words_result')
    content = []
    for j in text:
        content.append(j.get('words'))
    print(content)

def PathSetting():
    p = input("Use the default path by 'enter' Or input the path: ")

    if p == "":
        path = "/Users/Zoe/Desktop/snaptoword"
    else:
        path = p
    return (path)

'''def LanguageSetting():
    lang = input("Selecting English by enter 'eng' \t Selecting Chinese by enter 'chi'")
    return (lang)
'''
def New_All():
    key = input("Only convert the newest file: y; Converty all files: n \n")
    return (key)

# invoke the tesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.0/bin/tesseract'

# set up the link to Baidu account
APP_ID = '11293265'
API_KEY = 'FczPa3jOrR8pOkERD057nykE'
SECRET_KEY = 'U9GiGICphWGMsQzkB8ngXWuGkoTspW2W'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


# save the pic in the file
flag = "1"
while (flag =="1"):
    path = PathSetting()
    key = New_All()

    if key == 'n':
        for files in os.listdir(path):
            try:
                filename = os.path.join(path, files)
                convert (filename, client)
            except IOError:
                print ("cannot convert", files)
 
    else:
        file_time = 0
        last_file = ''
        for files in os.listdir(path):
            filename = os.path.join(path, files)
            if file_time < os.path.getctime(filename):
                file_time = os.path.getctime(filename)
                last_file = filename
            

        if last_file != '':
            try:
                convert (last_file, client)
            except IOError:
                print ("cannot", files)

    flag = input("Continue by enter '1'; \t Exit by enter '0'")

exit()


