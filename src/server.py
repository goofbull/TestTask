import socket
import time
from typing import Tuple
from generate_file import generate_file
import sys


def server_program():
    # Создаем хост и порт
    sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Создание UDP сокета
    host: str = 'localhost'
    port: int = 5000  # Выбор порта
    buffer_size: int = 1024  # Размер буффера

    sock.bind((host, port))  # Привязка адреса хоста и порта
    
    # Получаем размер файла из командной строки
    if len(sys.argv) < 2:
        print("Usage: python server.py <file_size>")
        sys.exit(1)
    try:
        file_size: int = int(sys.argv[1])
    except ValueError:
        print("Error: file size must be an integer")
        sys.exit(1)
    
    generate_file(file_size)  # Генерируем файл со случайным наполнением

    addr: Tuple[str, int]
    data: bytes
    data, addr = sock.recvfrom(buffer_size)  # Получаем пустое сообщение
    print(f'{addr} has been connected to the server')

    # Читаем файл для последующей отправки клиенту
    with open('random_file.txt', 'rb') as file:
        print('opening the file...')
        while chunk := file.read(buffer_size):  # Читаем файл чанками, т.к максимальный размер udp пакета - 65,507 байт
            sock.sendto(chunk, addr)
            time.sleep(0.001)  # Даем время между отправками чанков, чтобы не было перегруза

    sock.sendto(b'end', addr)  # Отсылаем сообщение, что это конец файла
    sock.close()  # Завершаем сеанс
    file.close()  # Закрываем файл
    print('the file has been sent')

if __name__ == '__main__':
    server_program()