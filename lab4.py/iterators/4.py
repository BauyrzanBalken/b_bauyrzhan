def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a = int(input())
b = int(input())

print(a,b)
for square in squares(a, b):
    print(square)