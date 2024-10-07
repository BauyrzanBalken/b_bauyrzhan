import math

def dr(d):
    return d * (math.pi / 180)

d = float(input("Input degree: "))

r = dr(d)


print(f"Output radian: {r:.6f}")