import socket


def server_program():
    # Создаем хост и порт
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создание TCP сокета
    port = 5000  # Выбор порта
 
    sock.bind(('localhost', port))  # Привязка адреса хоста и порта

    sock.listen(2)  # Конфигурируем сколько всего клиентов смогут прослушивать сервер одновременно
    
    conn, address = sock.accept()  # Принимаем новое подключение
    print("connection from: " + str(address))

    filename = 'random_file.txt'
    
    with open(filename, 'rb') as file:
        print('opening the file...')
        data = file.read(2*1024*1024)  # Читаем 2 мегабайта
        conn.send(data)  # Отсылаем файл

    file.close()  # Закрываем файл
    print('the file has been sent')
    conn.close()  # Завершаем сессию

if __name__ == '__main__':
    server_program()