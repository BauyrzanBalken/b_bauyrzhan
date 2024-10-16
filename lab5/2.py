#напишите программу на Python, которая соответствует строке, 
# за которой следует буква `a" и две-три буквы `b".
import re

def match_ab_two_to_three(s):
    return re.fullmatch(r'ab{2,3}', s) is not None


print(match_ab_two_to_three("abb"))   # True
print(match_ab_two_to_three("abbb"))  # True
print(match_ab_two_to_three("a"))     # False
print(match_ab_two_to_three("abbbbb"))# False