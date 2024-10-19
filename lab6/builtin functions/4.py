#Напишите программу на Python, которая вызывает функцию квадратного корня через определенные миллисекунды.
#Пример ввода:
#25100
#2123
#Примерный результат:
#Квадратный корень из 25100 через 2123 миллисекунды равен 158,42979517754858
import time
import math

def sqrt_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000)  # Преобразуем миллисекунды в секунды
    return math.sqrt(number)

print(f"Square root of 25100 after 2123 milliseconds is {sqrt_after_milliseconds(25100, 2123)}")
# Результат: Square root of 25100 after 2123 milliseconds is 158.42979517754858
