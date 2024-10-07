from datetime import datetime,timedelta
today = datetime.now()
tomorrow = today + timedelta(days = 1)
yesterday = today - timedelta(days = 1)
print(yesterday)
print(today)
print(tomorrow)