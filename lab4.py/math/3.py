import math

def p(n, s):
    return (n * s**2) / (4 * math.tan(math.pi / n))

n= int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

a = p(n, s)

print(f"The area of the polygon is: {a:.2f}")