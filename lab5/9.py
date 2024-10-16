#Напишите программу на Python для вставки пробелов между словами, начинающимися с заглавных букв.
def insert_spaces(s):
    return re.sub(r'([A-Z])', r' \1', s).strip()


print(insert_spaces("HelloWorldExample"))  # "Hello World Example"
