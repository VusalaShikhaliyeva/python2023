import datetime

# d = datetime.date(2024, 1, 8)
#
# print(d)
# print(type(d))
#
# today = datetime.date.today()
# print(today)
# print(today.year)
# print(today.month)
# print(today.day)
# print(f'{today.day}.{today.month}.{today.year}')
# print(d.weekday())
# print(d.isoweekday())
# print(type(today - d))
#
# tdelta = datetime.timedelta(days = 5, hours = 10)
#
# bday = datetime.date(2024, 3, 16)
# print((bday - today).total_seconds())
#
# tdelta = datetime.timedelta(days=12, minutes=13, hours=5).total_seconds()
# print(tdelta)
#
# t = deltatime.time(12, 32, 45, 12312)
# print(t.hour)
# print(t.minute)
# print(t.second)
# print(t.microsecond)
#
# now = datetime.timedelta(hours=3)
# print(t - tdelta)

dt = datetime.datetime(2024, 1, 1, 12, 30, 32, 123123)
print(dt)
print(type(dt))

today = datetime.datetime.utc()
print(today)

