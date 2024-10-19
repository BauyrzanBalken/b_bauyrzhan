#Напишите программу на Python со встроенной функцией,
#которая принимает строку и вычисляет количество прописных и строчных букв
def count_upper_lower(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return upper, lower

s = "Hello World!"
upper, lower = count_upper_lower(s)
print(f"Upper case: {upper}, Lower case: {lower}")  # Upper case: 2, Lower case: 8
