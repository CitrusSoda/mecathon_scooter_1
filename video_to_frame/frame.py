import cv2

count = 0

for i in range(1, 35):
    vidcap = cv2.VideoCapture(
        f'C:\\Users\\dndhk\\Downloads\\labelling\\video\\mecathon{i}.mp4')

    while(vidcap.isOpened()):
        ret, image = vidcap.read()

        if not ret:
            break

        if(int(vidcap.get(1)) % 5 == 0):
            cv2.imwrite(
                f"C:\\Users\\dndhk\\Downloads\\labelling\\picture\\frame{count}.jpg", image)

            print('Saved frame%d.jpg' % count)
            count += 1

    vidcap.release()
