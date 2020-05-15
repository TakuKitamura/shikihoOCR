from PIL import Image
import cv2
import pyocr
import pyocr.builders
import sys
import os
from janome.tokenizer import Tokenizer
t = Tokenizer()

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))

def absoluteFilePaths(directory):
    dic_list = []
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            dic_list.append(os.path.abspath(os.path.join(dirpath, f)))
            # yield os.path.abspath(os.path.join(dirpath, f))
    return dic_list

files = absoluteFilePaths('out/2') + absoluteFilePaths('out/15')

# 最大173
point = 0
for file_path in files[0:10]:

    img = cv2.imread(file_path)

    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
    # closing = cv2.morphologyEx(img_gray, cv2.MORPH_OPEN, kernel) 
    #closing = cv2.dilate(img_gray,kernel,iterations = 1)
    # 150 = 725pt
    # 170 = 19pt
    # 175 = 22pt
    # 180 = 22pt
    # 185 = 18pt
    # 186.5 = 15pt
    # 187.5 = 13pt
    # 188.5 = 14pt
    # 190 = 17pt
    # 210 = 103pt
    # 230 = 1162pt
    th, im_th = cv2.threshold(img, 187.5, 255, cv2.THRESH_BINARY)

    tmpFilePath = 'tmp/{}'.format(file_path.replace('/', '-'))
    cv2.imwrite(tmpFilePath, im_th)

    txt = tool.image_to_string(
        Image.open(tmpFilePath),
        lang='jpn_vert',
        builder=pyocr.builders.TextBuilder()
    )

    with open('05-15-00-44-09.txt', mode='a') as f:
        print(file_path)
        extract_text = txt.replace('\n', '')
        print(extract_text)
        print(len(extract_text))
        point += abs(len(extract_text)-173)
        # point += len(t.tokenize(extract_text))
        # print('len: {}'.format(len(extract_text)))
        print('total_point: {}'.format(point))
        # print('point: ',len(t.tokenize(extract_text)))
        # for v in t.tokenize(extract_text):
        #     print(v)
        print()

        f.write(file_path + '\n')
        f.write(extract_text+ '\n')
        f.write(str(len(extract_text))+ '\n')
        f.write('total_point: {}'.format(point)+ '\n')
        f.write('\n')
