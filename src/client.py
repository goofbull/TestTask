import socket


def client_program():
    # Создаем хост и порт
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создание TCP сокета
    port: int = 5000  # Выбираем порт

    print('connecting to server...')
    sock.connect(('localhost', port))  # Присоединение к серверу

    filename: str = 'received_file.txt'

    with open(filename, 'wb') as file:
        print('the downloading has started')
        data = sock.recv(2*1024*1024)  # Читаем 2 мегабайта
        file.write(data)  # Записываем содержимое

    file.close()  # Закрываем файл
    print('done downloading')

    sock.close()  # Завершаем сеанс

if __name__ == '__main__':
    client_program()