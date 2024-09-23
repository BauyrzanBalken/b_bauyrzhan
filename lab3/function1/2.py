def celsius(fah):
    return (5 / 9) * (fah - 32)


fah = float(input("Введите температуру в Фаренгейтах: "))
print(f"{fah}°F = {celsius(fah):.2f}°C")