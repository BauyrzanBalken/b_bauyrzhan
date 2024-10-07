def c(n):
    while n >= 0:
        yield n
        n -= 1 

n = int(input())

print(n)
for number in c(n):
    print(number)