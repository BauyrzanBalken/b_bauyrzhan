#Напишите программу на Python, которая соответствует строке, 
#за которой следует буква `a", заканчивающаяся на `b".
def match_a_anything_b(s):
    return re.fullmatch(r'a.*b', s) is not None


print(match_a_anything_b("ab"))      # True
print(match_a_anything_b("acb"))     # True
print(match_a_anything_b("abc"))     # False
