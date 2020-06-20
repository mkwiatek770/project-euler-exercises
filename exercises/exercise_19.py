"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import datetime
from dateutil.relativedelta import relativedelta

# intuitive approach

DAY = datetime.timedelta(days=1)
WEEK = datetime.timedelta(days=7)
MONTH = relativedelta(months=+1)
FIRST_DAY_OF_CENTURY = datetime.datetime(1901, 1, 1)
LAST_DAY_OF_CENTURY = datetime.datetime(2000, 12, 31)
current_date = FIRST_DAY_OF_CENTURY

counter = 0
while current_date <= LAST_DAY_OF_CENTURY:
    if current_date.weekday() == 6:
        counter += 1
    current_date += MONTH

print(counter)