import os

fileSizeInBytes = 2*1024*1024  # Размер файла 2 МБ

with open('random_file.txt', 'wb') as fout:  # Создаем файл случайного наполнения в размере 2 мегабайта
    fout.write(os.urandom(fileSizeInBytes))