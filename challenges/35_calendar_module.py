import calendar
month, day, year = map(int, input().split())
print(list(calendar.day_name)[calendar.weekday(year, month, day)].upper())