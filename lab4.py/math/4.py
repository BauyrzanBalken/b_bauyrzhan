def parallelogram_area(b, h):
    return b * h


b = float(input("Length of base: "))
h = float(input("Height of parallelogram: "))


area = parallelogram_area(b, h)


print(f"Expected Output: {area:.1f}")