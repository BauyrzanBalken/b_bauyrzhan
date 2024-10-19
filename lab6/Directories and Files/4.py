#Напишите программу на Python для подсчета количества строк в текстовом файле
def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)


file_path = "example.txt" 
print(f"Number of lines: {count_lines_in_file(file_path)}")
