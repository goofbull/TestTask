#!/bin/bash

cd ..
cd src
python generate_file.py
python server.py &
sleep 1
python client.py 

file_to_send="random_file.txt"
file_to_receive="received_file.txt"

if cmp -s "$file_to_send" "$file_to_receive"; then
    printf 'The file "%s" is the same as "%s"\n' "$file_to_send" "$file_to_receive"
else
    printf 'The file "%s" is different from "%s"\n' "$file_to_send" "$file_to_receive"
fi