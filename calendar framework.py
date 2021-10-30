import calendar
import datetime
import time

print(calendar.weekheader(2))

print(calendar.firstweekday())

print(calendar.month(2021,2))

print(calendar.calendar(2021))

print(calendar.monthcalendar(2021,2))

day_of_the_week = calendar.weekday(2021,2,4)
print(day_of_the_week)

is_leap = calendar.isleap(2020)
print(is_leap) 

how_many_leapday = calendar.leapdays(2000,2001)
print(how_many_leapday)

how_many_leapday = calendar.leapdays(2000,2005)
print(how_many_leapday)


