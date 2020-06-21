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
# DAY = datetime.timedelta(days=1)
# WEEK = datetime.timedelta(days=7)
MONTH = relativedelta(months=+1)
FIRST_DAY_OF_CENTURY = datetime.datetime(1901, 1, 1)
LAST_DAY_OF_CENTURY = datetime.datetime(2000, 12, 31)


def number_of_first_sundays(since=FIRST_DAY_OF_CENTURY, to=LAST_DAY_OF_CENTURY) -> int: 
    current_date = since
    counter = 0
    while current_date <= to:
        if current_date.weekday() == 6:
            counter += 1
        current_date += MONTH
    return counter


# Solution without using datatime library

def number_of_first_sundays_2():
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    l = [0, 1, 0, 0, 0, 0, 0]
    counter = 0
    for year in range(1901, 2001):
        if year % 4 == 0 and year % 100 == 0:
            months[1] = 29
        else:
            months[1] = 28
        for m in range(12):
            if l[0] == 1:
                counter += 1
            for _ in range(months[m]):
                l = [l[-1]] + l[:-1]
    return counter


if __name__ == '__main__':
    print(number_of_first_sundays())
