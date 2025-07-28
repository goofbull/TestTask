import socket


def client_program():
    # Создаем хост и порт
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Создание UDP сокета
    host = 'localhost'
    port: int = 5000  # Выбираем порт
    buffer_size: int = 1024  # Размер буффера

    sock.sendto(b'', (host, port))  # Отправляем пустое сообщение, чтобы подключиться к серверу

    # Создаем файл для записи
    filename: str = 'received_file.txt'
    with open(filename, 'wb') as file:
        print('the downloading has started')
        while True:
            data, addr = sock.recvfrom(buffer_size)
            if data == b'end':
                break
            file.write(data)
            
    file.close()  # Закрываем файл
    print('done downloading')

    sock.close()  # Завершаем сеанс

if __name__ == '__main__':
    client_program()