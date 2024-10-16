#Напишите программу на Python для поиска последовательностей из одной заглавной буквы,
#за которой следуют строчные буквы.
def match_upper_lower(s):
    return re.fullmatch(r'[A-Z][a-z]+', s) is not None


print(match_upper_lower("Hello"))  # True
print(match_upper_lower("HELLO"))  # False
print(match_upper_lower("H"))      # False
