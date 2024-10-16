#Напишите программу на Python для разбиения строки на заглавные буквы.
def split_at_uppercase(s):
    return re.split(r'(?=[A-Z])', s)


print(split_at_uppercase("HelloWorldExample"))  # ['Hello', 'World', 'Example']
