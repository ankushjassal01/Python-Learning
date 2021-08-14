"""
Python provide three modules to deal with data and time - time, datetime and calender
with dealing with time/date we need to understand the localisation and data its saving/where its saving
majority of word works on UTC timezones its singularity around which all the countries clocks run +/- the time
* when we are dealing with elapse time like how much time program took to work then we will use the TIME module.
* if dealing with dates and time then DATETIME will be useful
# below are the functions/methods of the time modules
DESCRIPTION
    There are two standard representations of time.  One is the number
    of seconds since the Epoch, in UTC (a.k.a. GMT).  It may be an integer
    or a floating point number (to represent fractions of seconds).
    The Epoch is system-defined; on Unix, it is generally January 1st, 1970.
    The actual value can be retrieved by calling gmtime(0).

    The other representation is a tuple of 9 integers giving local time.
    The tuple items are:
      year (including century, e.g. 1998)
      month (1-12)
      day (1-31)
      hours (0-23)
      minutes (0-59)
      seconds (0-59)
      weekday (0-6, Monday is 0)
      Julian day (day in the year, 1-366)
      DST (Daylight Savings Time) flag (-1, 0 or 1)
    If the DST flag is 0, the time is given in the regular time zone;
    if it is 1, the time is given in the DST time zone;
    if it is -1, mktime() should guess based on the date and time.

    Variables:

    timezone -- difference in seconds between UTC and local standard time. Its negative if country is east to the
                Greenwich meridian. positive for west and for UK its 0, usage None for DST.
    altzone -- difference in  seconds between UTC and local DST time
    daylight -- whether local time should reflect DST
    tzname -- tuple of (standard time zone name, DST time zone name)

    Functions:

    time() -- return current time in seconds since the Epoch as a float
    clock() -- return CPU time since process start as a float
    sleep() -- delay for a number of seconds given as a float
    gmtime() -- convert seconds since Epoch to UTC tuple
    localtime() -- convert seconds since Epoch to local time tuple
    asctime() -- convert time tuple to string
    ctime() -- convert time in seconds to string
    mktime() -- convert local time tuple to seconds since Epoch
    strftime() -- convert time tuple to string according to format specification
    strptime() -- parse string to time tuple according to format specification
    tzset() -- change the local timezone

    below are for the strptime /strftime
        %a Locale’s abbreviated weekday name.
        %A Locale’s full weekday name.
        %b Locale’s abbreviated month name.
        %B Locale’s full month name.
        %c Locale’s appropriate date and time representation.
        %d Day of the month as a decimal number [01,31].
        %H Hour (24-hour clock) as a decimal number [00,23].
        %I Hour (12-hour clock) as a decimal number [01,12].
        %j Day of the year as a decimal number [001,366].
        %m Month as a decimal number [01,12].
        %M Minute as a decimal number [00,59].
        %p Locale’s equivalent of either AM or PM.
        %S Second as a decimal number [00,61].
        %U Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new
           year preceding the first Sunday are considered to be in week 0.
        %w Weekday as a decimal number [0(Sunday),6].
        %W Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new
           year preceding the first Monday are considered to be in week 0.
        %x Locale’s appropriate date representation.
        %X Locale’s appropriate time representation.
        %y Year without century as a decimal number [00,99].
        %Y Year with century as a decimal number.
        %z Time zone offset indicating a positive or negative time difference from UTC/GMT of the form +HHMM or -HHMM,
           where H represents decimal hour digits and M represents decimal minute digits [-23:59, +23:59].
           this will not give same result on all platform as all ANSI C library do not support this.
        %Z Time zone name (no characters if no time zone exists). (it is deprecated now so better not to use)
        %% A literal '%' character.

for elapse time use perf_counter to measure it rather then time()/monotonic().
for process time/cpu execution time for process use process_time.
PEP: python enhancement proposal


"""
import time
print(time.tzname)  # tuple of timezone/DST timeZone
print(time.timezone)  # difference between UTC and local timezone
print(time.daylight)
print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))
print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))
if time.daylight != 0:
    print("\tDaylight Saving Time (DST) is defined for this location")
    print("\tThe DST timezone name is " + time.tzname[1])
print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print("UTC is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))

# help(t)
print(time.clock())
# for i in dir(time):
#     if i[0] != '_':
#         print(i)
#     # if i[0] == '_':
#     #     print(i)
#     #     for x in dir(i):
#     #         print(x)
#     #     print('*' * 20)

print(time.gmtime(0))  # this gives the epoch time. its the time from C it is stored as start time. time before that can
#                      # deal as the negative and it might not easy to deal with
#                      # it convert it into tuple and always works in UTC.
print(time.gmtime())   # it gives the current UTC time compare to local timezone date.
print(time.localtime())  # its the time of the system its running/if we put any args in localtime() then it print epoch
#                        # its convert the output to tuple
print(time.time())  # it print the number of second since the start of epoch date(1970)
#
time_here = time.localtime()  # time_here have the named tuple values so it can be called below
print(time_here)
print("Year:", time_here[0], time_here.tm_year)  # here due to named tuple we are calling it using indexing and as well
print("Month:", time_here[1], time_here.tm_mon)  # As named tuple method like time_here.tm_mon, time_here.tm_sec
print("Day:", time_here[2], time_here.tm_mday)
########################################################################################################################

import time  # time module to use all the methods of module
# here my_timer is time() function from the time module.
from time import time as my_timer,monotonic as timer,perf_counter as perf,process_time as pt
import random  # random module

input("Press enter to start")  # to start the game

wait_time = random.randint(1, 6)  # it will give the random number between 1 to 6
time.sleep(wait_time)  # Delay execution for a given number of seconds.  The argument may be
#                      # a floating point number for subsecond precision.
start_time = my_timer()  # using time() function here
start_times = timer()
start_tim = perf()
start_tm = pt()
input("Press enter to stop")  # to stop the game and evaluate the result/elapse time

end_time = my_timer()  # using time() function here
end_times = timer()
end_tim = perf()
end_tm = pt()

# strftime: convert time tuple to string according to format specification
# strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))
print(time.strptime('Thu Jan 14 18:05:32 2021', "%c"))  # just for the example run
print(time.localtime(end_time))
print("Your reaction time was {} seconds".format(end_time - start_time))

# monotonic:
# monotonic clock time cant goes backward like Day light saving thing.its rules out any adjustment due to day light
# saving.Adjustment to computer time will not affect the time returned by the code
print('monotonic time')
print(time.localtime(start_times))
print("Ended at " + time.strftime("%X", time.localtime(end_times)))
print("Your reaction time was {} seconds".format(end_times - start_times))

# perf_Counter is most precise clock.its used by trace and time module to get idea of performance of the func we write
# it have higher resolution in some system.its also cannot be go back( no DST)
print('perf_counter time')
print("Started at " + time.strftime("%X", time.localtime(start_tim)))
print("Ended at " + time.strftime("%X", time.localtime(end_tim)))
print("Your reaction time was {} seconds".format(end_tim - start_tim))

# process_time shows the time spent by CPU executing the current process rather then elapse time.
print('process_time')
print("Started at " + time.strftime("%X", time.localtime(start_tm)))
print("Ended at " + time.strftime("%X", time.localtime(end_tm)))
print("Your reaction time was {} seconds".format(end_tm - start_tm))
########################################################################################################################

"""
# get_clock_info(str_name)
# it give the info of the different clocks like below
# get information on the specified clock as a namespace object
time.clock() :'clock'
time.time() :'time'
time.monotonic() :'monotonic'
time.perf_counter() :'perf_counter'
time.process_time() :'process_time'
* adjustable: True if the clock can be changed automatically (e.g. by a NTP daemon) or manually by the system 
  administrator, False otherwise
* implementation: The name of the underlying C function used to get the clock value. Refer to Clock ID Constants for 
  possible values.
* monotonic: True if the clock cannot go backward, False otherwise
* resolution: The resolution of the clock in seconds (float)
"""

print("time():\t\t\t", time.get_clock_info('time'))
print("perf_counter():\t", time.get_clock_info('perf_counter'))
print("monotonic():\t", time.get_clock_info('monotonic'))
print("process_time():\t", time.get_clock_info('process_time'))
print("clock():\t\t", time.get_clock_info('clock'))
########################################################################################################################
# datetime module:
# if we are dealing with the date and time then its better to use the datetime module rather the time module but time
# also provide the dates but its better to use datetime as it have more methods for that.

import datetime
# date objects are naive and datetime objects are aware of timezone offset
# below first datetime is module and 2nd one is class. this is how we can access the class methods in module.
print(datetime.datetime.today())  # Today time in 12 hour format
print(datetime.datetime.now())  # current time. Now() and today() will give same result but now can give result
#                               # according to timezone(TZ= none) 12 hour format. if timezone given then 24 hour format
print(datetime.datetime.utcnow().tzinfo)  # UTC time for current local time


'''
datetime have below methods
MAXYEAR
MINYEAR
date
datetime  class object
datetime_CAPI
time
timedelta
timezone
tzinfo

datetime.datetime class have below methods.
astimezone
combine
ctime
date
day
dst
fromordinal
fromtimestamp
hour
isocalendar
isoformat
isoweekday
max
microsecond
min
minute
month
now
replace
resolution
second
strftime
strptime
time
timestamp
timetuple
timetz
today
toordinal
tzinfo
tzname
utcfromtimestamp
utcnow
utcoffset
utctimetuple
weekday
year

'''





