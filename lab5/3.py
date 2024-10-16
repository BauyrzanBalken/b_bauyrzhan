#нАпишите программу на Python для поиска последовательностей строчных букв,
# соединенных символом подчеркивания.
import re
def find_lowercase_underscore(s):
    return re.fullmatch(r'[a-z]+_[a-z]+', s) is not None


print(find_lowercase_underscore("abc_def"))  # True
print(find_lowercase_underscore("abc_Def"))  # False
print(find_lowercase_underscore("abc_defg")) # True
