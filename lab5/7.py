#Напишите программу на python для преобразования строки в регистре snake в строку в регистре camel.
def snake_to_camel(s):
    return re.sub(r'(_[a-z])', lambda x: x.group(1)[1:].upper(), s)

print(snake_to_camel("snake_case_example"))  # "snakeCaseExample"
