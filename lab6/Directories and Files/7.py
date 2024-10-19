#Напишите программу на Python для копирования содержимого файла в другой файл
def copy_file(src, dst):
    with open(src, 'r') as src_file:
        content = src_file.read()
    with open(dst, 'w') as dst_file:
        dst_file.write(content)

# Example usage:
copy_file("source.txt", "destination.txt")
