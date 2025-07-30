import socket
import sys


def client_program() -> None:
    # Создаем хост и порт
    sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создание TCP сокета
    port: int = 5000  # Выбираем порт
    
    print('connecting to server...')
    sock.connect(('localhost', port))  # Присоединение к серверу

    # Получаем размер файла из командной строки
    if len(sys.argv) < 2:
        print("Usage: python server.py <file_size>")
        sys.exit(1)
    try:
        file_size: int = int(sys.argv[1])
    except ValueError:
        print("Error: file size must be an integer")
        sys.exit(1)

    filename: str = 'received_file.txt'
    with open(filename, 'wb') as file:
        print('the downloading has started')
        while True:
            data: bytes = sock.recv(file_size)  # Получаем содержимое файла
            if not data:  # Если данных нет, выходим из цикла
                break
            file.write(data)  # Записываем содержимое

    file.close()  # Закрываем файл
    print('done downloading')
    sock.close()  # Завершаем сеанс

if __name__ == '__main__':
    client_program()