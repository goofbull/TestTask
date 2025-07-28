import socket
import time


def server_program():
    # Создаем хост и порт
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Создание UDP сокета
    host = 'localhost'
    port: int = 5000  # Выбор порта
    buffer_size: int = 1024  # Размер буффера

    sock.bind((host, port))  # Привязка адреса хоста и порта

    data, addr = sock.recvfrom(buffer_size)  # Получаем пустое сообщение
    print(f'{addr} has been connected to the server')

    # Читаем файл для последующей отправки клиенту
    filename: str = 'random_file.txt'
    with open(filename, 'rb') as file:
        print('opening the file...')
        while chunk := file.read(buffer_size):  # Читаем файл чанками, т.к максимальный размер udp пакета - 65,507 байт
            sock.sendto(chunk, addr)
            time.sleep(0.001)  # Даем время между отправками чанков, чтобы не было перегруза

    sock.sendto(b'end', addr)  # Отсылаем сообщение, что это конец файла
    sock.close()  # Заывершаем сеанс
    file.close()  # Закрываем файл
    print('the file has been sent')

if __name__ == '__main__':
    server_program()