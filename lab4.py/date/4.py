from datetime import datetime
d1 = input("Введите(YYYY-MM-DD HH:MM:SS): ")
d2 = input("Введите(YYYY-MM-DD HH:MM:SS): ")

date1 = datetime.strptime(d1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(d2, "%Y-%m-%d %H:%M:%S")

dif = date2 - date1

difsec = dif.total_seconds()
print(f"Разница между датами в секундах: {difsec} секунд.")
