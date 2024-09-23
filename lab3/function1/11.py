def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

s = input("Введите слово или фразу: ")
print(is_palindrome(s))