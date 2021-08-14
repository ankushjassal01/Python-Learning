# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import datetime
import pytz

# zone_list = []
#
#
# def zones():
#     for zone in pytz.all_timezones:
#         if zone[:3] == 'US/':
#             zone_list.append(zone)
#             print(zone)
#
#
# while True:
#     choice = input("please choose the timezone from above OR Type '0' to quit: ".format(zones()))
#     if choice in zone_list:
#         zone = pytz.timezone(choice)
#         local_time = datetime.datetime.now(zone)
#         utc_time = pytz.utc.localize(datetime.datetime.utcnow())
#         # print('Your Chosen Timezone Have Date & Time & timezone as :{} and Timezone Name as {}'.format(local_time.
#         # strftime('%A %x %X %Z'), local_time.tzinfo))
#         print('Your Chosen Timezone Have Date & Time & timezone as :{} '.format(local_time.strftime('%A %x %I:%M:%S  '
#                                                                                                     '%p %z %Z')))
#         print('Your Chosen Timezone Have Date & Time & timezone as :{}'.format(utc_time.strftime('%A %x %I:%M:%S %p  '
#                                                                                                  '%z %Z')))
#     elif choice == '0':
#         print('You are out of program')
#         break
#     else:
#         print('\tYour Choice is either wrong or have typo error. Please choose again correctly:\n\n')

########################################################################################################################
# Program by udemy instructor
available_zones = {'1': "Africa/Tunis",
                   '2': "Asia/Kolkata",
                   '3': "Australia/Adelaide",
                   '4': "Europe/Brussels",
                   '5': "Europe/London",
                   '6': "Japan",
                   '7': "Pacific/Tahiti",
                   '8': "US/Hawaii",
                   '9': "Zulu"}

print("Please choose a time zone (or 0 to quit):")
for place in sorted(available_zones):
    print("\t{}. {}".format(place, available_zones[place]))

while True:
    choice = input()

    if choice == '0':
        break

    if choice in available_zones.keys():
        tz_to_display = pytz.timezone(available_zones[choice])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {} {}".format(available_zones[choice], world_time.strftime('%A %x %X %z'), world_time.
                                               tzname()))
        print("Local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))

