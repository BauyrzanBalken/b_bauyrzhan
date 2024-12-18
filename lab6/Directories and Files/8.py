#Напишите программу на Python для удаления файла по указанному пути. 
#Перед удалением проверьте наличие доступа и то, существует ли указанный путь или нет.
import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            os.remove(file_path)
            print(f"File {file_path} deleted.")
        else:
            print(f"Access denied to {file_path}.")
    else:
        print(f"File {file_path} does not exist.")


delete_file("example.txt")
