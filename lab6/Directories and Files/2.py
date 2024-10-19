#апишите программу на Python для проверки доступа к указанному пути. 
#Проверьте наличие, читаемость, возможность записи и выполнения указанного пути
import os

def check_access(path):
    print(f"Checking access for: {path}")
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))


path = "."  
check_access(path)
