import pickle
# pickle is pre defined library for this pickling thing in python


# Pickle is same as serialisation in Java. Its way to store or restore objects in files to use it for later
# Python provide the way to serialisation the objects called pickling/pickle
# when the object is pickled then it written to the file format that  contain the objects data together with the
# sufficient information that allow that object to be recreated  when loaded back in.

# pickle is not secure with the malicious contents because if we pass some commands which leads to delete the files
# during loading the files then it can cause file removal.it warning for untrusted source. load can execute code.
# Also pickle have drawback that objects all need to load data back to OS memory. It is not an issue for small objects
# but for large objects like dict of large items then it can cause issue in memory allocation


imelda = ('More Mayhem',
          'IMelda May',
          '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))

with open("imelda.pickle", "ba") as pickle_file:  # with ba or ab mode it append the data in pickle dump file but
    pickle.dump(imelda, pickle_file)  # when we retrieve it by rb or br it will show only one main data file which we
    #                                 # dump into the pickle file.
    # pickle.dump used to write the data in the pickle file to save it in binary data file. the data will be written
    # along with the some binary code/bytes
    # dump('object which you want to pickle/to_binary' , 'file/file alias in which you want to add' )


with open("imelda.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)  # pickle.load is used to load/read the data from the pickle file to another
    #                                      # variable
    # print(pickle.load(imelda_pickled)) also works same as assigning its value to variable

print(imelda2 )

album, artist, year, track_list = imelda2

print(album)
print(artist)
print(year)
for track_number, track_title in track_list:  # unpacking of track_list at for loop definition.
    # track_number, track_title = track  # unpacking in indentation of for loop
    print(track_number, track_title)

# Multiple Objects pickling
# below we are pickling multiple objects to same pickle file
# NOTE: when we call them then we need to load/read it back in the order they are defined in the pickle file
# like if object 1, object 2 , object 3 are dumped in order then load() should be in same order too.
# if not loaded back in order like object2 call ina available/print first then it wont give error . instead of that it
# will load the first object to that print/object ,it might cause issue in the o/p order or data which you want to store
with open("imelda.pickle", "rb") as imelda_pickled:
    #imelda2 = pickle.load(imelda_pickled)
    even_list = pickle.load(imelda_pickled)  # here only even_list is called so it will add imelda file in variable
    #odd_list = pickle.load(imelda_pickled)
    #x = pickle.load(imelda_pickled)

# only few objects are which might be saved by pickle process in python but majorities can be saved by this process

imelda = ('More Mayhem',
          'IMelda May',
          '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)  # protocol is not necessary in pickling
    pickle.dump(even, pickle_file, protocol=0)
    pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(2998302, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
# protocols are used in pickle to dump more data in the file or large data file/objects in the pickle file
# NOTE: Protocols arent backward version compatible. like if protocol ver 4 used in 3.4 might not be valid in python 3.5
# protocol=0 was first protocol and it save data in more user readable format.
# protocol=1 was first binary protocol . All version of python should able to unpickle data created with this protocol
# protocol=2 this introduced in python 2.3. It can pickle class more efficiently but it declared insecure
# protocol=3 it is default protocol if not specified. It comes in python 3 version. the file which are created with it
# can be easily readable in py 3 but not in py ver 2
# we can use different protocol in same file like above.
with open("imelda.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)
    even_list = pickle.load(imelda_pickled)
    odd_list = pickle.load(imelda_pickled)
    x = pickle.load(imelda_pickled)

print(imelda2)

album, artist, year, track_list = imelda2

print(album)
print(artist)
print(year)
for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)

print('=' * 40)

for i in even_list:
    print(i)

print('=' * 40)

for i in odd_list:
    print(i)

print('=' * 40)

print(x)

print('=' * 40)

# below will lead to remove the file from the system.
pickle.loads(b"cos\nsystem\n(S'del imelda2.pickle'\ntR.")     # windows











