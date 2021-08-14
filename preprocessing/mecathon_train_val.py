count = 0
length = 3081

txt = open(r"C:\Users\dndhk\Downloads\shuffle.txt", 'r', encoding='UTF-8')

i = 0

f = open(r"C:\Users\dndhk\Downloads\train.txt", 'w', encoding='UTF-8')
f2 = open(r"C:\Users\dndhk\Downloads\validation.txt", 'w', encoding='UTF-8')

while True:
    if i == 0:
        line = txt.readline()
        if not line:
            break
        count += 1
        if count < int(length/10):
            f2.write(line)
        else:
            f.write(line)

txt.close()
f.close()
f2.close()
