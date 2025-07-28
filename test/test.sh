#!/bin/bash

cd ..
cd src
python generate_file.py  # Запускаем генерацию файла со случайным наполнением
python server.py &  # Запускаем сервер в фоновом режиме
sleep 1             # Даем время на прогрузку
python client.py    # Запускаем клиентскую программу

file_to_send="random_file.txt"
file_to_receive="received_file.txt"

# Сравниваем сгенерированный файл и полученный
if cmp -s "$file_to_send" "$file_to_receive"; then
    printf 'The file "%s" is the same as "%s"\n' "$file_to_send" "$file_to_receive"
else
    printf 'The file "%s" is different from "%s"\n' "$file_to_send" "$file_to_receive"
fi