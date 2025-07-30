import socket
from typing import Tuple


def client_program():
    # Создаем хост и порт
    sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Создание UDP сокета
    host: str = 'localhost'
    port: int = 5000  # Выбираем порт
    buffer_size: int = 1024  # Размер буффера

    sock.sendto(b'', (host, port))  # Отправляем пустое сообщение, чтобы подключиться к серверу

    with open('received_file.txt', 'wb') as file:  # Записываем данные в файл
        print('the downloading has started')
        while True:
            data: bytes
            addr: Tuple[str, int]
            data, addr = sock.recvfrom(buffer_size)
            if data == b'end':
                break
            file.write(data)
            
    print('done downloading')

    sock.close()  # Завершаем сеанс

if __name__ == '__main__':
    client_program()