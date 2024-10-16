#Напишите программу на Python, которая соответствует строке,
#за которой следует буква `a" и ноль или более букв `b".
import re

def match_ab_zero_or_more(s):
    return re.fullmatch(r'ab*', s) is not None


print(match_ab_zero_or_more("ab"))   # True
print(match_ab_zero_or_more("a"))    # True
print(match_ab_zero_or_more("abb"))  # True
print(match_ab_zero_or_more("ac"))   # False
