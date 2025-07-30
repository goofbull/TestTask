#!/bin/bash

cd ..
cd src
read -p "Input file size in bytes: " file_size  # Вписываем размер файла
python server.py "$file_size" &  # Запускаем сервер в фоновом режиме, передаем размер файла
sleep 2             # Даем время на прогрузку
python client.py "$file_size"  # Запускаем клиентскую программу, передаем размер файла

file_to_send="random_file.txt"
file_to_receive="received_file.txt"

# Сравниваем сгенерированный файл и полученный
if diff "$file_to_send" "$file_to_receive"; then
    printf 'The file "%s" is the same as "%s"\n' "$file_to_send" "$file_to_receive"
else
    printf 'The file "%s" is different from "%s"\n' "$file_to_send" "$file_to_receive"
fi