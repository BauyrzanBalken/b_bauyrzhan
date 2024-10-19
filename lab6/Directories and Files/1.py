#Напишите программу на Python, 
#которая будет отображать только каталоги, файлы и все каталоги
#файлы по указанному пути
import os

def list_directories_files(path):
    directories = []
    files = []
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            directories.append(entry)
        elif os.path.isfile(full_path):
            files.append(entry)

    print("Directories:", directories)
    print("Files:", files)


path = "." 
list_directories_files(path)
