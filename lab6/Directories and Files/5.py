#Напишите программу на Python для записи списка в файл.
def write_list_to_file(data_list, file_path):
    with open(file_path, 'w') as file:
        for item in data_list:
            file.write(f"{item}\n")

# Example usage:
data_list = ['apple', 'banana', 'cherry']
file_path = "fruits.txt"
write_list_to_file(data_list, file_path)
