#Напишите программу на Python для преобразования заданной строки регистра camel в регистр snake.
def camel_to_snake(s):
    return re.sub(r'([A-Z])', r'_\1', s).lower().lstrip('_')


print(camel_to_snake("camelCaseExample"))  # "camel_case_example"
