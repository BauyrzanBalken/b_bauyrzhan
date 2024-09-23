from itertools import permutations

def print_permutations(s):
    perms = permutations(s)
    for perm in perms:
        print(''.join(perm))


s = input("Введите строку: ")
print_permutations(s)