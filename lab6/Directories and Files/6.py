#Напишите программу на Python для создания 26 текстовых файлов с именами A.txt, B.txt и так далее до Z.txt
import string

def generate_text_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            file.write(f"This is {letter}.txt")

# Example usage:
generate_text_files()
