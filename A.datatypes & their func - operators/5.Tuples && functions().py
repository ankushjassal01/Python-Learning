# %%Tuples
# similar to list
# ORDERED Sequenece of objects
# does support SLICING/INDEXING
# does not support ITEM ASSIGNMENT WITH INDEXING
# tup[2]=(1,2)  gives error
# CONCATENATION works tup=tup +(1,2) +(1,2) or tup=tup +(1,2) or
# tup=tup +(1,2) +(1,2,[1,2],{'a':'val'}) all works except below
# but pure tup+ pure list or pure dict or pure float or pure str or pure int wont works
# (# its case for all the datatypes)
# tup=tup +(4) -- it alone int thats why error But
# during variable creation and its assignment if we are adding like this : 
# tup=(1) or tup=(1.4) or tup=('class') or tup (['class','class]) or tup=({'class':'class'}) 
# then dont think it makes it as Tuples :
# parenthesis does not make it tuples.for Tuples objects need to be more then 1 and
# if start with list or dict the it should contain another list or dict inside paranathesis
# tup=(['class','class'],['class','class']) or tup=({'class':'class'},{'class':'class'}) or 
# tup=({'class':'class'},({'class':'class'}))
# enclosed inside the ()
# INDEXING WORKS WITH RESPECT TO THE DATATYPE IT HAVE.SAME AS FUNCTIONS.
# IF WE WANT TO CHECK THE DATA INSIDE DIFFERENT DATATYPE THEN ::
# LIST CONTAINS THE DICT THEN FIRST LIST INDEX WORKS THEN TO CHECK DICT KEY
# IF THEY KEY CONTAIN LIST OR SOMEELSE THEN ITS INDEX OR KEY ACCORDING TO DATA IT HAVE
# SAME FOR FUCNCTIONS. IF THAT FUNCTION DONT WORK AT THAT DATATYPE INDEX THEN IT SHOULD NOT
# BE CALLED
# can contain the MULTIPLE DATATYPES str, float, multiple lists , lists, dict, dicts, tuples inside tuples
# WHEN TO USE THE TUPLE AND WHEN TO USE THE LIST
# as we know that both can be unpack but if our requirement is to have immutable values
# tuple if not then list. like if append something in list then it increase it size and 
# we cannot use it to unpacking . so tuple is where size is fixed and cannot be change
Tup=(1,2,[1,2,'cls',{'a':(1,'cls')}],{"a":{"b":(1,'cls')}},(1,2))
print(Tup[2][3]["a"][1][0])
print(Tup[2][3]["a"][1])
print(Tup[2][3]["a"])
print(Tup[2][3])
print(Tup[2])
print(Tup)

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not
# recognize it as a tuple.
# One item tuple, remember the commma ,
print()
thistuple = ("apple",)
print(type(thistuple))
print(thistuple)
a=1,2,4,5 # without bracket it can also create the tuple as comma used
print(a)
print(type(a)) # it is tuple
## new tupel with tuple
tuples=(1,2)
t=tuples,1, # this way concatination works too in the tuple
print(t)

# when we just type any other datatype with comma it makes it to form a tuple like below
lists=[1,2]
l=lists,1,2# here we are adding 1,2 in list but it not addiing in list , it making tuple

print(l) #([1,2],1,2)
print(type(l)) # tuple
l='ss'
n=l,2
print(n) # ('ss',2)
print(type(n)) # tuple

# The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists
# %% tuple unpacking / SEQUENCE UNPACKING
# unpacking can be useful in API i believe , we can get the values and return them
# in diff variables
# also in CSV data load files and  they have defined number of rows
x,y,z=1,2,5 # here 1,2,5are tuple elements and printing x y z is sort of unpacking
print(x)
print(y)
print(z)
A=1,2,3,
print ('tuple unpacking')
print(A)
a,b,c=A # here A is assigned to a,b,c by tuple unpacking
print(a)
print(b)
print(c)
# enumerate also use the tuple unpacking Values
# we can unpack any sequence 
print('unpack the list')
A=[1,2,4,]
B=['ab','CD','DE']
print(A)
a,b,c=A
print(a)
print(b)
print(c)
print('unpack the list')  # list unpacking wont used due to lists are mutable and once changed the unpacking wont work
a,b,c=B # unpack the list
print(B)
print(a)
print(b)
print(c)
print('unpack the String')
A='ANK' # unpack the string
a,b,c=A
print(A)
print(a)
print(b)
print(c)
print('unpack the SET')
A={1,2,4,}
a,b,c=A
print(A)
print(a)
print(b)
print(c)
print('unpack the DICT')
A={1:'a',2:'c',4:'D'} # dict will unpack the keys only 
a,b,c=A.items()
print(A.items())
print('item() will makes the tuples and we are doing indexing of below ')
print(a)
print(a[0])
print(a[1])
print(b)
print(b[0])
print(b[1])
print(c)
print(c[0])
print(c[1])
print()
a,b,c=A.values()
print(A.values())
print(a)
print(b)
print(c)
print()
a,b,c=A.keys()
print(A.keys())
print(a)
print(b)
print(c)
print('multiple unpacking in loop of dict.value() ..first key and then value datatype unpacking and it value')
# here we are doing unpacking of values of each keys by tuple unpacking.
x={'F_name': 'Ankush', 'L_name': 'Jassal', 'class': 'twelth'}
for key,value in x.items():
    print(key)
    print(value)
    print()

# here we are doing unpacking of values of each keys by tuple unpacking.
# its looks like two unpacking, first keys and its values and then in values again
# values are unpacked according to length that's why (a,b,c,d,e,f)
# unpacking but make sure length of values are same in each key. if not then unpacking
# fail and give error like ValueError: not enough values to unpack (expected 6, got 5)
for key,(a,b,c,d,e,f) in x.items():
    print(key)
    print(a)  # only taking value of one
    print()


# A=[(1,3)(2,4)(6,5)]
# print(A) # give error as 'tuple' object is not callable ,why because it tuples are not separated by comma
A=[(1,3),(2,4),(6,5)] # this is correct way of defining multiple tuples
print(A)
# %% Tuple Length
# To determine how many items a tuple has, use the len() method:
# Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) 

# %%Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:
# Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") 
  
# %% Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into
# a tuple.
# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# %% The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
# Example
# Using the tuple() method to make a tuple:
this_tuple = tuple(["apple", "banana", "cherry"])  # note the square brackets
print(this_tuple)  # ('apple', 'cherry', 'banana')
this_tuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(this_tuple)  # ('apple', 'cherry', 'banana')
this_tuple = tuple({"apple", "banana", "cherry"})  # note the curly braces
print(this_tuple)  # ('apple', 'cherry', 'banana')
this_tuple = tuple({'A': "apple", 1: "banana", 'C': "cherry"})  # note the curly braces
print(this_tuple)  # ('A', 1, 'C')


# %%count()	Returns the number of times a specified value occurs in a tuple
# The count() method returns the number of times a specified value appears in the tuple.
# Syntax
# tuple.count(value)
# Parameter Values
# Parameter 	Description
# value 	Required. The item to search for

# Return the number of times the value 5 appears in the tuple:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5, (5,6))
x = thistuple.count(5)
print(x) 

# %%index()	Searches the tuple for a specified value and returns the position of where it was found
# The index() method finds the first occurrence of the specified value.
# The index() method raises an exception if the value is not found.
# Syntax
# tuple.index(value)
# Parameter Values
# Parameter 	Description
# value 	Required. The item to search for

# Search for the first occurrence of the value 8, and return its position:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)  # only first instance not furthers
x = thistuple.index(8)
print(x) 
