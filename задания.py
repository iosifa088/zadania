from datetime import  datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
#1
from datetime import datetime

date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 2, 1)
delta = date2 - date1
days_diff = delta.days

print(days_diff)
#2
from datetime import datetime

date = datetime(2024, 1, 15)
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
day_name = days[date.weekday()]
print(day_name)
#3
from datetime import datetime, date

birth_date = datetime(1990, 5, 15).date()
today = date.today()

def calculate_age(birth_date):
    age = today.year - birth_date.year
    if today < date(today.year, birth_date.month, birth_date.day):
        age -= 1
    return age

print(calculate_age(birth_date))
#4
from datetime import datetime, timedelta

current_date = datetime(2024, 1, 15)
next_day = current_date + timedelta(days=1)
print(next_day.strftime("%Y-%m-%d"))
#5
from datetime import datetime, timedelta

date = datetime(2024, 2, 15)

def last_day_of_month(d):
    if d.month == 12:
        next_month = datetime(d.year + 1, 1, 1)
    else:
        next_month = datetime(d.year, d.month + 1, 1)
    last_day = next_month - timedelta(days=1)
    return last_day.day

print(last_day_of_month(date))
#6
import time

def slow_function():
    time.sleep(2)

start_time = time.time()
slow_function()
end_time = time.time()

print(f"Время выполнения: {end_time - start_time:.2f} секунд")
#7
from datetime import datetime

date_str = "2024-01-15 14:30:00"
dt_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(dt_obj)
#8
dt = datetime(2024, 1, 15, 14, 30, 45)

format1 = dt.strftime("%d/%m/%y")
format2 = dt.strftime("%Y-%m-%d")
format3 = dt.strftime("%B %d, %Y")

print(format1)
print(format2)
print(format3)
#9
import calendar

year = 2024
is_leap = calendar.isleap(year)
print(is_leap)
#10
