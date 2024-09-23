def sphere_volume(radius):
    return (4/3) * 3.14159265359 * radius**3


radius = float(input("Введите радиус сферы: "))
print(f"Объем сферы: {sphere_volume(radius)}")