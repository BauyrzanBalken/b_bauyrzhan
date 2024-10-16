#Напишите программу на Python, которая заменит все пробелы, запятые или точки на двоеточие.
def replace_with_colon(s):
    return re.sub(r'[ ,.]', ':', s)


print(replace_with_colon("Hello, world. How are you?"))  # "Hello: world: How are you?"
