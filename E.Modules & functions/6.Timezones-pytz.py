'''
datetime.tzinfo timezone definitions generated from the
Olson timezone database:

    ftp://elsie.nci.nih.gov/pub/tz*.tar.gz

See the datetime section of the Python Library Reference for information
on how to use these modules.
It fetch timezones from IANA:Internet Assigned named authority they maintain the Timezones.
'''

import pytz
import datetime

# country = 'Europe/Kiev'
#
# tz_to_display = pytz.timezone(country)
# print(tz_to_display)
# local_time = datetime.datetime.now(tz=tz_to_display)
# print("The time in {} is {}".format(country, local_time))
# print("UTC is {}".format(datetime.datetime.utcnow()))

# pytz.all_timezones> contain the all the timezone names which are available on the server
for x in pytz.all_timezones:
    print(x)
########################################################################################################################
# Its a Dict of {country code:country name }. Its gave the dict and its value result if used in for
# print(pytz.country_names)  with direct print it wont print whole dict as it should be but it print its memory location
for x in sorted(pytz.country_names):
    print(x + ": " + pytz.country_names[x])
#######################################################################################################################
# pytz.country_timezones
# it gave the dict of country code and its different time zones as a list. it gave the all the timezone a country have.
# like US have many Timezones. DE ['Europe/Berlin', 'Europe/Busingen']. It may contain all the country code or not.
for x in sorted(pytz.country_timezones):
    print(x ,pytz.country_timezones[x])
########################################################################################################################

# getting the country with its code and country name and its all timezones
for x in sorted(pytz.country_names):
    print('{}: {}:{}'.format(x,pytz.country_names[x],pytz.country_timezones.get(x)))

# getting the country code and country name and its timezones and its local time.
# UA: Ukraine: Have timeZones & time below:
# Europe/Kiev                   :2021-01-17 19:47:47.495234+02:00
# Europe/Simferopol             :2021-01-17 20:47:47.495234+03:00
for x in sorted(pytz.country_names):
    print("{}: {}: Have timeZones & time below:".format(x, pytz.country_names[x]))
    # below condition to check that if country code in timezones function
    if x in pytz.country_timezones:
        # print(pytz.country_timezones[x])
        for zone in sorted(pytz.country_timezones[x]):
            # check if
            if len(pytz.country_timezones[x]) > 1:
                tz_to_display = pytz.timezone(zone)
                local_time = datetime.datetime.now(tz=tz_to_display)
                print("\t{0:<30}:{1}".format(zone, local_time))
            elif len(pytz.country_timezones[x]) == 1:
                tz_to_display = pytz.timezone(zone)
                local_time = datetime.datetime.now(tz=tz_to_display)
                print("\t{0} and time is {1}".format(zone, local_time))
    else:
        print("\t\tNo time zone defined")

########################################################################################################################
import datetime
import pytz
print(datetime.datetime.utcnow().tzinfo)  # None because utcnow() dont have tz
# always works in UTC timezone , only change to local time if we need time to display to user.
# always store the time with its timezone.
kiev = pytz.timezone('Europe/Kiev')
print(kiev.zone)
# local_time = datetime.datetime.now(kiev)
local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time {}".format(local_time))
print("Naive UTC {}".format(utc_time))
print('#'*120)
########################################################################################################################
# localize()
# it convert the naive date time to aware date time but it may be UTC as timezone but datetime will be correct.
# it add the offset hours in the end of datetime output.
# localize use naive datetime with no timezone information. It set the timezone to UTC but dont give time to UTC until
# UTC provided by editor. It can also gave error if aware time passed as argument. like if localtime have already
# mentioned the timezone like this local_time = datetime.datetime.now(kiev) then it cannot be used in the localize().
aware_local_time = pytz.utc.localize(local_time)  # it gave o/p as : 2021-01-18 01:58:17.870861+00:00  >-time may differ
aware_utc_time = pytz.utc.localize(utc_time)  # it gave o/p as : 2021-01-18 06:58:17.870861+00:00
print("Aware local time {}, time zone {} ".format(aware_local_time, aware_local_time.tzinfo))
print("Aware UTC {}, time zone {}".format(aware_utc_time, aware_utc_time.tzinfo))
print('#'*120)
########################################################################################################################
# astimezone(tzname=None) Its from the datetime, time
# it gave the current datetime timezone like (+/- UTC hours). It can take the tzname as argument if not given then it
# will give the local time timezone info detail
# it decreaseincrease the datetime according to its system timezone but with tzinfo object it will give correct timezone
# but it also alter the localtime/utc time according to its timezone offset hours. like if offset is -05:00 hours then
# it will give local time as -5 hour and utc time also -5. See below:
# eastern timezone: local time will be 2021-01-18 02:02:55.118307+00:00 gave time offset as UTC hour +00:00 but time
# will be correct.UTC will be 2021-01-18 07:02:55.118307+00:00 but when we apply the astimezone() it gave result of
# local time as 2021-01-17 21:02:55.118307-05:00 and UTC 2021-01-18 02:02:55.118307-05:00 but it have now eastern
# timezone offset hour as its timezone.earlier it was not showing.
# it cannot applied to naive time/datetime ie. dont have timezone included , only applied to aware time/datetime
# tzinfo > it gave the output as its timezone info it extract the timezone offset hours and find it respecting timezone
# name and gave it name as output. like Eastern Standard Time, Indian Standard Time
aware_local_time = pytz.utc.localize(local_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time).astimezone()
print("Aware local time {}, time zone {} ".format(aware_local_time, aware_local_time.tzinfo))
print("Aware UTC {}, time zone {}".format(aware_utc_time, aware_utc_time.tzinfo))
print('#'*120)
########################################################################################################################
# datetime.datetime(year, month=None, day=None, hour=0, minute=0, second=0,microsecond=0,tzinfo=None)> output as defined
# datetime objects timestamp. o/p: 2021-01-18 03:14:34.511146
eastern = pytz.timezone('US/Eastern')
gap_time = datetime.datetime.now()
g = datetime.datetime.now(eastern)
print(gap_time)
print(g)
# Timestamp() > it give the time as in second from the epoch. like this :1610959495.732815
print(gap_time.timestamp())
print(g.timestamp())  # both g.timestamp() and gap_Time.timestamp are same because they have been accounted from the
# localtime.
s=gap_time.timestamp()
t = s + (60 * 60)
print('#'*50)

########################################################################################################################
# fromtimestamp(t, tz=None)  > It gave the current local time timestamp.it only take the t as seconds not any standard
# time stamp also can take the timezone. it will be in 12 hour format.No TZ info
print(datetime.datetime.fromtimestamp(s))
dt1 = pytz.utc.localize(datetime.datetime.fromtimestamp(s)).astimezone(eastern)  # timezone given to astimezone() func
dt2 = pytz.utc.localize(datetime.datetime.fromtimestamp(t)).astimezone(eastern)
print("{} seconds since the epoch is {}".format(s, dt1))
print("{} seconds since the epoch is {}".format(t, dt2))
dt1 = pytz.utc.localize(datetime.datetime.fromtimestamp(s)).astimezone(eastern)  # timezone given to astimezone() func
dt2 = pytz.utc.localize(datetime.datetime.fromtimestamp(t)).astimezone(eastern)
print("{} seconds since the epoch is {}".format(s, dt1))
print("{} seconds since the epoch is {}".format(t, dt2))
print('#'*120)
########################################################################################################################
# utcfromtimestamp(t)> It gave the o/p as timestamp but it will be in UTC hour , the offset will be added or septracted
# to become UTC hours it take the t as seconds not any standard time stamp.12 hour format. No TZ info .
# it will check local time
print(datetime.datetime.utcfromtimestamp(s))
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(eastern)  # timezone given to astimezone so
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(eastern)  # local tz
print("{} seconds since the epoch is {}".format(s, dt1))
print("{} seconds since the epoch is {}".format(t, dt2))
print('#'*120)
########################################################################################################################

'''
pytz have below methods
AmbiguousTimeError
BaseTzInfo
FixedOffset
HOUR
InvalidTimeError
LazyDict
LazyList
LazySet
NonExistentTimeError
OLSEN_VERSION
OLSON_VERSION
UTC   class object
UnknownTimeZoneError
VERSION
ZERO
all_timezones
all_timezones_set
ascii
build_tzinfo
common_timezones
common_timezones_set
country_names
country_timezones
datetime
exceptions
lazy
open_resource
os
resource_exists
sys
timezone
tzfile
tzinfo
unicode
unpickler
utc
*************************************************
pytz.utc have below methods:
dst
fromutc
localize
normalize
tzname
utcoffset
zone

********************************************************
import datetime
import pytz
for i in dir(datetime):
    if i[0] != '_':
        print(i)



for i in dir(pytz):
    if i == 'BaseTzInfo':
        # print(help(pytz.BaseTzInfo))
        for x in dir(pytz.BaseTzInfo):
            print(x)
        print('*' * 20)
'''