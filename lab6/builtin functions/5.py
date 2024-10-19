#Write a Python program with builtin function that returns True if all elements of the tuple are true.
def all_elements_true(tup):
    return all(tup)

tup = (True, True, False)
print(all_elements_true(tup))  # Результат: False
