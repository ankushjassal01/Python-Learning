# Write file
# we can write into file by w mode of opening a file
# we can write by write() or with file keyword of print
# writing to file is little tricky as it overwrite the file content. so without correct options it can cause issue
# print will not give any message but you can write some kind of print to make sure its done like print('done')
with open('dummy.txt', 'w') as b:
    print('this is dummy file and new line has been added and another added', file=b)
    print('done first add')

with open('dummy.txt', 'r') as c:
    print(c.read())  # it show new blank  line at the end of the output of file as it was written with print with file.
    #                # below print will be at blank line
    print('*****1st overwritten file output*****')
    print(c.read(), end='')  # double read in same with wont give output
    print('*****1st overwritten file output*****')
# print will write any kind of data to the file but that will change to a string. its just works like a .format method
# see line 92 onwards
# ******************************************************************************************************************** #
# write can only take the strings . not others data types like list or list[str] etc
cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]

with open('dummy.txt', 'w') as b:
    for i in cities:
        print(i, file=b) # it add to file as it open in w mode
with open('dummy.txt', 'r') as c:
    print(c.read())
    print('*****1st.A overwritten file output*****')

# ******************************************************************************************************************** #
with open('dummy.txt', 'w') as b:
    for i in cities:
        b.write('{} '.format(i))  # here this write overwrite the above written values to dummy.txt
    b.writelines('\nthis is new line\n')  # but writelines will not overwrite the files it will add the another value
    b.writelines('\ndummy line')  # to the file either increase or in new line but only in same with command
#                                 # writelines also overwrite if used alone on already written file like below

with open('dummy.txt', 'r') as c:
    print(c.read())
    print('*****2nd overwritten file output*****')

# here appending will be done for each line but /n line of 2nd line will taken in the 0 index here and then follow on
# also if if extra \n used then it will add as object at its index position
d = []
with open('dummy.txt', 'r') as c:
    for i in c:  # ['Adelaide Alice Springs Darwin Melbourne Sydney \n', 'this is new line\n', 'dummy line']
        d.append(i)
print(d)

# ******************************************************************************************************************** #
with open('dummy.txt', 'w') as b:
    b.writelines('this is 3rd line')  # for write or writelines  use 'w' mode

with open('dummy.txt', 'r') as c:
    print(c.read())
    print('*****3rd overwritten file output*****')

# ******************************************************************************************************************** #
# writelines can take list contains strings only.. it should not contain tuple or tuple containing string etc
# but the input of that list[str] will pass as string without spaces
# write and writelines both do not print lines to new lines. it print to same line and have no spaces
with open('dummy.txt', 'w') as b:
    print(b.writelines(cities))  # print with write will give none but the written function already affect the file
    print(b.writelines(['this is command']))
    # print(b.writelines([' \nthis is command'])) if this used then o/p will be
    # AdelaideAlice SpringsDarwinMelbourneSydney
    # this is command

with open('dummy.txt', 'r') as c:
    print(c.read())
    print('*****4th overwritten file output*****')

# if we append the any written files data to a list then it wont written as a string indexing it written as a whole
# line to a string

d = []

with open('dummy.txt', 'r') as c:
    for i in c:  # also these files do not follows the rules of indexing although they have strings ,cannot use indexing
        d.append(i)  # ['AdelaideAlice SpringsDarwinMelbourneSydneythis is command']
        # for the /n of above writeline commented line appending o/p
        # ['AdelaideAlice SpringsDarwinMelbourneSydney \n', 'this is command']

print(d)
d = []

# ******************************************************************************************************************** #
with open('dummy.txt', 'w') as b:
    b.write('this is first line')

with open('dummy.txt', 'r') as c:
    for i in c:  # ['this is first line']
        d.append(i)

print(d)

# ******************************************************************************************************************** #

imelda = "More Mayhem", "Imelda MAy", "2011", (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

with open("imelda3.txt", 'w') as imelda_file:
    print(imelda, file=imelda_file)  # it written tuple to file but it will be as string
#                                    # with print we can add any datatype to the file

with open("imelda3.txt", 'r') as imelda_file:
    contents = imelda_file.readline()
    print(contents)
    print(type(contents))  # <class 'str'>
imelda = eval(contents) # with eval we can take the same datatype as its showing actually. still not sure about eval()
print(imelda)
print(type(imelda))  # <class 'tuple'>
imelda = ["More Mayhem", "Imelda MAy", "2011", (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))]

with open("imelda3.txt", 'w') as imelda_file:
    # imelda_file.write(imelda)  it wont work as write() wont accept the anything else then string
    print(imelda, file=imelda_file)
    # imelda_file.writelines(imelda) it also wont works it should list[str] only not tuple

# this is easy way to write the logging for the program . it can write the steps which our program  follows

# ******************************************************************************************************************** #
# eval() function
# it evaluate any string to any expression
with open("imelda3.txt", 'r') as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)