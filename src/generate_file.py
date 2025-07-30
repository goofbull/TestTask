import os


def generate_file(fileSizeInByte: int) -> None:
    with open('random_file.txt', 'wb') as fout:  # Создаем файл случайного наполнения в выбранном размере
        fout.write(os.urandom(fileSizeInByte))