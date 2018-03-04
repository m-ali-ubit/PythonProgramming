
import time         # include time module
import calendar     # include calender module

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
