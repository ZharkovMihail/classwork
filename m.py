# Программа для чтения видео
# и извлечь кадры

import cv2, os  # подключаем нужные модули
import subprocess
# Функция для извлечения кадров

def FrameCapture(path):
    # Путь к видеофайлу

    vidObj = cv2.VideoCapture(path)

    count = 0

    success = 1

    while success:
        # vidObj объект вызывает чтение

        # функция извлечения кадров

        success, image = vidObj.read()

        # Сохраняет кадры с количеством кадров
        try:

            cv2.imwrite("frame%d.jpg" % count, image)

        except :

            print("That key does not exist!")

        count += 1


def makevideo():


    out = cv2.VideoWriter("/home/apulazo/PycharmProjects/cutiing_video/video1.mp4", 0x7634706d, 30, (640, 360))  # создаем видео
    for i in range(50):
        out.write(cv2.imread(f"/home/apulazo/PycharmProjects/cutiing_video/frame{i}.jpg"))  # добавляем картинки
    out.release()  # генерируем
    cv2.destroyAllWindows()  # завершаем

if __name__ == '__main__':
    # Вызов функции

    FrameCapture("/home/apulazo/PycharmProjects/cutiing_video/Atoms - 13232.mp4")
    makevideo()
    #subprocess.call("/home/apulazo/PycharmProjects/cutiing_video/video.avi", shell=True)