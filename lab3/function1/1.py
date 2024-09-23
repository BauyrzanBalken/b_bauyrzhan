def ounces(gr):
    return gr * 28.3495231

gr = float(input("Введите количество граммов: "))
print(f"{gr} грамм = {ounces(gr)} унций")