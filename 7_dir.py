

import os
import time


for path, direct, files in os.walk('.'):

    for ff in files:
        filepath = path

        dir = os.path.join(path, ff)

        filetime = os.path.getmtime(dir)
        format_time = time.strftime("%d.%m.%Y %H:%M",time.localtime(filetime))

        filesize = os.path.getsize(dir) / 1024
        print(f" Обнаружен файл {ff}, Путь : {dir} , Размер {filesize :.2f} байт, Время изменения :{format_time}, "
              f"Родительская директория {os.path.dirname(dir)} ")