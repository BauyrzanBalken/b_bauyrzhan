#Напишите программу на Python, чтобы проверить, 
#существует ли заданный путь. Если путь существует, 
#найдите имя файла и часть каталога в заданном пути.
import os

def check_path(path):
    if os.path.exists(path):
        directory, filename = os.path.split(path)
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print("The path does not exist.")


path = "/path/to/file.txt"  
check_path(path)
