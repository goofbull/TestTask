import socket
import sys
from typing import Tuple
from generate_file import generate_file


def server_program() -> None:
    # Создаем хост и порт
    sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создание TCP сокета
    port: int = 5000  # Выбор порта
 
    sock.bind(('localhost', port))  # Привязка адреса хоста и порта

    sock.listen(2)  # Конфигурируем сколько всего клиентов смогут прослушивать сервер одновременно

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

    conn: socket.socket
    address: Tuple[str, int]
    conn, address = sock.accept()  # Принимаем новое подключение
    print("connection from: " + str(address))

    filename: str = 'random_file.txt'
    
    with open(filename, 'rb') as file:
        print('opening the file...')
        data = file.read(file_size)  # Получаем файл
        conn.send(data)  # Отсылаем файл

    file.close()  # Закрываем файл
    print('the file has been sent')
    sock.close()  # Закрываем сессию
    conn.close()  # Отключаемся

if __name__ == '__main__':
    server_program()