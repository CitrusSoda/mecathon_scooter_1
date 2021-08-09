import os
import random

path = r"C:\Users\dndhk\Downloads\mecathon_data"
file_list = os.listdir(path)
file_list_jpg = [image for image in file_list if image.endswith(".jpg")]

random.shuffle(file_list_jpg)

f = open(r"C:\Users\dndhk\Downloads\shuffle.txt", 'w', encoding='UTF-8')

for name in file_list_jpg:
    f.write(r'/content/gdrive/Shareddrives/메카톤2021여름/mecathon/darknet/custom/img/' + name + '\n')

f.close()
