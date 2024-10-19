#Напишите программу на Python со встроенной функцией для умножения всех чисел в списке
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

numbers = [2, 3, 4, 5]
print(multiply_list(numbers))  # Результат: 120
