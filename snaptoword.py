from PIL import Image
import pytesseract
import os, sys
import time, datetime

def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

#default path：
p = input("Use the default path by 'enter' Or input the path: ")

if p == "":
    path = "/Users/Zoe/Desktop/snaptoword"
else:
    path = p

# invoke the tesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.0/bin/tesseract'

# selection of language
lang = input("Selecting English by enter 'eng' \t Selecting Chinese by enter 'chi'")

# get the image and convert to the string. 
def convert(file_name, lang_type):
    if lang_type == 'eng':
        lang = 'eng'
    elif lang_type == 'chi':
        lang = 'chi_sim'
    elif (lang_type != 'eng') & (lang_type != 'chi'):
        print ("invalid language, will use English as default.")
        lang = 'eng'
    image = Image.open(file_name)
    content = pytesseract.image_to_string(image, lang)   # 解析图片
    print(content + '\n')

# only the newest, or all file?
key = input("Only convert the newest file: y; Converty all files: n \n")

# save the pic in the file
if key == 'n':
    for files in os.listdir(path):
        try:
            filename = os.path.join(path, files)
            convert (filename, lang)
        except IOError:
            print ("cannot convert", files)
 
else:
    file_time = 0
    last_file = ''
    for files in os.listdir(path):
        filename = os.path.join(path, files)
        print(files, TimeStampToTime(os.path.getctime(filename)))
        if file_time < os.path.getctime(filename):
            file_time = os.path.getctime(filename)
            last_file = filename
            

    if last_file != '':
        try:
            convert (last_file, lang)
        except IOError:
            print ("cannot", files)
     


# get the import as the pic

