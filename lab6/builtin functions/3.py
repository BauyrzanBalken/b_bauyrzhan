#Напишите программу на Python со встроенной функцией,
#которая проверяет, является ли переданная строка палиндромом или нет.
def is_palindrome(s):
    return s == s[::-1]

s = "madam"
print(is_palindrome(s))  # Результат: True
