import os
import random

path = r"C:\Users\dndhk\Downloads\custom\img"
file_list = os.listdir(path)
file_list_jpg = [image for image in file_list if image.endswith(".jpg")]
file_list_txt = [text for text in file_list if text.endswith(".txt")]

jpg_names = []
for jpg_name in file_list_jpg:
    if jpg_name.count(".") == 1:
        name = jpg_name.split(".")[0]
        jpg_names.append(name)

text_names = []
for text_name in file_list_txt:
    if text_name.count(".") == 1:
        name = text_name.split(".")[0]
        text_names.append(name)

for jpg in jpg_names:
    if jpg not in text_names:
        os.remove(path + r"\\" + jpg + '.jpg')
        print(jpg + '.jpg 파일이 제거되었습니다')
