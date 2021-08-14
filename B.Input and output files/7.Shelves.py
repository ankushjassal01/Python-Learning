""""# it provide the shelve for objects
# rather then storing data in memory it store data in Files. Its like Dict but it store data in Files
# like a dict it hold the key value pairs. values can be anything which can be pickled . Keys must be strings
# all the methods used in dict can be used in the shelves too.
# it have same warning as pickle for untrusted source. load can execute the code.
# shelve create three files.
# shelve first create a db file but i windows it wont show but its show in error. not quite sure about it
# file_name.dir > it store data in form of tuple.. key,(some int value tuple) but in any order like dict
# file_name.dat > it show data in format of binary i believe not properly readable.
# file_name.bak > it store data in form of tuple.. key,(some int value tuple) but in any order like dict
# shelves are read write (r,w) in nature so no need to define the mode.
# with mode 'a' it can also. it append data to the file. but watch out if file don't exist. it wont create new file
# we can also read it by print command ,r w or a mode.
# append the same data will not add the same data twice in the file but instead it alter the .dat,.bak,.dir files.
# read functions wont work.
# dont add mode 'r' or 'w' in shelve.open(). it auto assign it but if added then give error. but only if file not exist
# new file will give error
# NOTE:drawback of shelve
# it may not be suitable for some applications. because value being pickling before stored and unpickle when read back
# if values are very complex. it may impact the performance of the application.
# SO RATHER THE SHELVE OR PICKLE AS ORGANIZATION WE SHOULD SAVE DATA USING DATABASE TECHNIQUE AS THEY ARE IMMUTABLE TO
# SYSTEM REQUIREMENT AND TO UNTRUSTED FILES.THEY ARE EASY TO USE AND EASILY PORTABLE TO WEB/NEW SYSTEM ETC. ALTHOUGH
# SHELVE IS VERY MUCH HELPFUL BUT STORING LARGE QUANTITY DATA NOT A GOOD THING WITH IT. I BELIEVE FOR LOGGING IT IS EASY
# TO USE BUT THERE MAY BE BETTER OPTION FOR THIS ONE."""
import shelve
with shelve.open('ShelfTest') as fruit:
    # keys should be strings only but values can be any data type value
    fruit['orange'] = 'this is first fruit in shelve file'
    fruit['apple'] = 'I love to eat them'
    fruit['lemon'] = 'good for making cheese from milk'
    print(fruit['lemon'])
    print(fruit['orange'])

# with shelve.open('ShelfTest1') as fruit:
#     fruit={1:'1',2:1} # it wont work like that.it cannot add fruit dict to the shelve file.literal wont work like that

# %% with open/close() like file methods
# we cannot do operation like call dict[item] on shelve file alias/file after it closure.
# it Only work in indentation in With
# but if open in normal mode which need to close after use then it works like below

fruit = shelve.open('ShelfTest2')  # opened here
fruit['orange'] = "a sweet, orange, citrus fruit" # non indentation shelve pickling working here.
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"

print(fruit["lemon"])
print(fruit["grape"])
fruit.close() # closed here

print(fruit)

# in Shelves if we added the key wrongly then it can be added to the shelve file but we cannot call it by correct name:
# like below we added the key engin_size  ut we are calling it with engine_size and it gave error , we later corrected
# it to engine_size but it can added the same key to that
# it don't work like dict, in dict we can correct it rewrite the data to dict but not like below
# a["engin_size"]=a["engine_size"] , instead we can just correct it from beginning and reassign the variable to dict
# but in file/shelve once it written then we cannot correct it by correcting it and run file again. because wrong key
# already added  and file created. so do over come it we need to delete it and add correct one or add first then remove
# shelve is a file so it wont remove until removed it but not like with 'w' mode.

# In Shelves once it run then it either write or read or append or remove things from the shelves file till the line it
# get error. So be ready to remove removed one data from rerunning again as it already removed from file.
with shelve.open("bike2") as bike:
    # bike["make"] = "Honda"
    # bike["model"] = "250 dream"
    # bike["colour"] = "red"
    # bike['engin_size']=250
    # bike["engine_size"] = 250
    print(bike["engine_size"])  # we are calling it with
    print(bike["colour"])
    # del bike['engin_size']

    for key in bike:
        print(key)

    print('=' * 40)

    print(bike["engine_size"])
    # print(bike["engin_size"])
    print(bike["colour"])



