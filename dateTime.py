
import time         # include time module
import calendar     # include calender module
from datetime import date

# Number of ticks since 12:00am, January 1, 1970 (epoch)
ticks = time.time()
print(ticks)                            # 1516891779.6040437

print(time.localtime())                 # local time

print(time.timezone)                    # time zone

print(time.localtime(time.time()))      # current time

print(time.asctime(time.localtime(time.time())))    # formatted current time

print(time.clock())                     # current CPU time

print(time.ctime())                     # formatted current time using no. of seconds

# sleep function ; rest process for given seconds
print(time.ctime())                     # Thu Jan 25 20:05:25 2018
time.sleep(1)                           # sleep for 10 seconds
print(time.ctime())                     # Thu Jan 25 20:05:35 2018

print(calendar.calendar(2018))          # formatted calender of given year

print(calendar.firstweekday())          # 0 ; means monday

print(calendar.isleap(2018))            # returns True if year is leap year else False

print(calendar.month(2018, 1))          # whole formatted calender of given month

print(calendar.monthcalendar(2018, 1))  # returns list of lists as every week is a list

# pytz library is also a date time module which gives more functionality

# some basic logical functions


def days_in_month(year, month):                 # returns the number of days in given month

    if month == 12:
        days = date(year+1, 1, 1) - date(year, month, 1)
    else:
        days = date(year, month+1, 1) - date(year, month, 1)
    return days.days


def is_valid_date(year, month, day):            # check whether the given date is valid or not

    try:
        date(year, month, day)
        return True
    except ValueError:
        return False


def days_between(year1, month1, day1, year2, month2, day2):     # returns no. of days bw two valid dates

    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2):

        if date(year1, month1, day1) < date(year2, month2, day2):
            return (date(year2, month2, day2) - date(year1, month1, day1)).days
        else:
            return 0
    else:
        return 0


def age_in_days(year, month, day):              # returns the age in days till today

    today = date.today()
    if is_valid_date(year, month, day) and date(year, month, day) < today:
        return days_between(year, month, day, today.year, today.month, today.day)
    else:
        return 0
