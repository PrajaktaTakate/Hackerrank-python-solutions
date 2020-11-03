"""
input
08 05 2015
op-
WEDNESDAY
"""
import calendar
print(calendar.TextCalendar().formatyear(2020))

m, d, y = map(int, input().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())