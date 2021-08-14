# %%LIST
# ORDERED sequence of objects
# Mutable
A = [1]
print(id(A))
A = [1, 2, 3]
print(id(A))
A += [4]
print(A)
print(id(A))
B = A  # we aware what value you are puting for variable A=B or B=A , both are different
# in A=B, if B already exist then A value updated with A.
print(id(B))
# inclosed inside []
# support CONCATENATION of same datatypes only
# but pure list + pure list or pure dict or pure float or pure str or pure int wont works (# its case for all the datatypes)
# Can have MULTIPLE DATATYPES inside its
# INDEXING AND SLICING works
# ITEM ASSIGNMENT  works
# nested INDEXING works
# if dict inside the list then if want to call it then must use index first
# cannot use direct Key to call it like a=[{'a':1}]==a[0]['a'] this is correct method
# INDEXING WORKS WITH RESPECT TO THE DATATYPE IT HAVE.SAME AS FUNCTIONS.
# IF WE WANT TO CHECK THE DATA INSIDE DIFFERENT DATATYPE THEN ::
# LIST CONTAINS THE DICT THEN FIRST LIST INDEX WORKS THEN TO CHECK DICT KEY
# IF THEY KEY CONTAIN LIST OR SOMEELSE THEN ITS INDEX OR KEY ACCORDING TO DATA IT HAVE
# SAME FOR FUCNCTIONS. IF THAT FUNCTION DONT WORK AT THAT DATATYPE INDEX THEN IT SHOULD NOT
# BE CALLED
A = ['anksuh', 'Jassal']
print(A[1][0])
# A[0][1]="J" #it wont works due to python is also strongly typed . string will not have item assignement
A[0] = 'J'
A = [{'a': "b"}]
print(A[0]['a'])  # nested INDEXING
print(type(A[0]['a']))  # tyoe with nested INDEXING

even = [2, 4, 6, 8]
odd = [1, 3]
odd.extend([5, 7])  # extend should have all data in list or whatever the argument you pass
# it should be only one.if list only one, string only one
# odd.extend(5,7) # will  give argument error                  
print(odd)

A = even + odd
print(A)  # [2, 4, 6, 8, 1, 3, 5, 7]
B = sorted(A)  # sorted function
A.sort()  # sort list method
print(A)  # [1, 2, 3, 4, 5, 6, 7, 8] Here A was sorted with sorted with list sort method
print(B)  # [1, 2, 3, 4, 5, 6, 7, 8] Here B was sorted with built in sorted function
print(A is B)  # False Here A is not B because A identity and B identity is not same.
# there items are same but object not same
print(id(A))  # 309613392768
print(id(B))  # 309613299776
print(A == B)  # True Because items are same in the list objects

# Main diff b/w sort and sorted is that sort do not give the value. it just alter
# the original list. But Sorted gave the value but do not alter the original list
# sorted give the value in form of List. and list item depend on iteerable value
A = [3, 1, 9, 4]
sorted(A)  # this sorted dont affect the A
print(A)  # [3, 1, 9, 4]
print(id(A))
print()
B = sorted(A)  # this sorted bind its output to object Name B
print(B)  # [1, 3, 4, 9]
print(id(B))  # here A not equal to B
print(A == B)
print()
C = [3, 1, 9, 4]
print(C)
print(id(C))
print(C.sort())  # after sort due to mutable identity remain same # this Method return the None
print(C)
print(id(C))

# Case insensitive list sorting
# it need keyword which we learn later in functions
# syntax is key=method/function without()
A = 'Ankush Jassal'
B = sorted(A)
print(A)  # Ankush Jassal
print(B)  # [' ', 'A', 'J', 'a', 'a', 'h', 'k', 'l', 'n', 's', 's', 's', 'u']
# Sorted but Upper case letter first then lower case letters.
# to optimize it we use keyword
print(id(B))
B = sorted(A, key=str.casefold)
print(B)  # [' ', 'A', 'a', 'a', 'h', 'J', 'k', 'l', 'n', 's', 's', 's', 'u']
print(id(B))

# %% List Length
# To determine how many items a list has, use the len() function:
# Example

# Print the number of items in the list:
this_list = ["apple", "banana", "cherry"]
print(len(this_list))

# %% append()	Adds an element at the end of the list
# The append() method appends an element to the end of the list.
# list.append(elmnt)
# Parameter Values
# Parameter 	Description
# elmnt 	Required. An element of any type (string, number, object etc.)

# Add a list to a list:
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)  # if list append then list will appending inside list.

# Add an element to the fruits list:
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(a)
print(fruits)

# %% clear()	Removes all the elements from the list
# The clear() method removes all the elements from a list.
# list.clear()
# Parameter Values
# No parameters

# Remove all elements from the fruits list:
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()

# %% copy()	Returns a copy of the list
# The copy() method returns a copy of the specified list.
# Syntax
# list.copy()
# Parameter Value
# No parameters

# Copy the fruits list:
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)

# %% count()	Returns the number of elements with the specified value
# The count() method returns the number of elements with the specified value.
# Syntax
# list.count(value)
# Parameter Values
# Parameter 	Description
# value 	Required. Any type (string, number, list, tuple, etc.). The value to search for.

# Return the number of times the value "cherry" appears int the fruits list:
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)
# Return the number of times the value 9 appears int the list:
points = [1, 4, 2, 9, 7, 8, 9, 3, 1, [9, 5]]
x = points.count(9)

print(x)

# %% extend() Add the elements of a list (or any iterable), to the end of the current list
# The extend() method adds the specified list elements (or any iterable) to the end of the current list.
# Syntax
# list.extend(iterable)
# Parameter Values
# Parameter 	Description
# iterable 	Required. Any iterable (list, set, tuple, etc.)

# Add a tuple to the fruits list:
fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)  # its does add the tuplel or whatever is the datatype. 
# instead of that it add element of that in list as it is.. if some other dtattype inside that then it same will be printed
print(fruits)
# Add the elements of cars to the fruits list:
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', ['Volvo']]
fruits.extend(cars)
print(fruits)

A = {'a': 'class'}
fruits.extend(A)  # if dict then keys will be inserted in list not value unles we define the index
# ['apple', 'banana', 'cherry', 'Volvo', 'a']
print(fruits)
fruits.extend(A['a'])  # during dict if key contain string the it will parsed into iteration
# ['apple', 'banana', 'cherry', 'Volvo', 'c', 'l', 'a', 's', 's']
print(fruits)
B = 'class'  # alone string will also parse and added
# ['apple', 'banana', 'cherry', 'Volvo', 'c', 'l', 'a', 's', 's']
fruits.extend(B)
# fruits.extend(points[1]) # error as int are not iterable . it should be inside a list tupel but not alone
print(fruits)

A = [1, 2, 3, 'class']
B = ['class']  ## string inside list will not be parsed
A.extend(B)
print(A)

A = [1, 2, 3, 'class']
C = ('1', 'class')
A.extend(C)
print(A)
A.extend(C[1])  # string inside tuple can also be parsed if alone used
print(A)
A.extend('value')
print(A)

# %% index()	Returns the index of the first element with the specified value
# The index() method returns the position at the first occurrence of the specified value.
# Syntax
# list.index(elmnt)
# Parameter Values
# Parameter 	Description
# elmnt 	Required. Any type (string, number, list, etc.). The element to search for

# What is the position of the value 32:
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)
# What is the position of the value "cherry":
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)
# %% insert()	Adds an element at the specified position
# The insert() method inserts the specified value at the specified position.
# Syntax
# list.insert(pos, elmnt)
# Parameter Values
# Parameter 	Description
# pos 	Required. A number specifying in which position to insert the value
# elmnt 	Required. An element of any type (string, number, object etc.)

# Insert the value "orange" as the second element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.insert(0, "orange")  # uses index position 
print(fruits)

# %% pop()	Removes the element at the specified position
# The pop() method removes the element at the specified position.
# Syntax
# list.pop(pos)
# Parameter Values
# Parameter 	Description
# pos 	Optional. A number specifying the position of the element you want to remove, default value is -1, which returns the last item

# Return the removed element:
fruits = ['apple', 'banana', 'cherry']
x = fruits.pop()
print(x)

# Remove the second element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
print(fruits.pop(1))

# %% remove()	Removes the item with the specified value
# The remove() method removes the first occurrence of the element with the specified value.
# Syntax
# list.remove(elmnt)
# Parameter Values
# Parameter 	Description
# elmnt 	Required. Any type (string, number, list etc.) The element you want to remove

# Remove the "banana" element of the fruit list:
fruits = ['apple', 'banana', 'cherry', 'banana']
fruits.remove("banana")  # only first occurrence . not further ones
print(fruits)

# %% reverse()	Reverses the order of the list
# The reverse() method reverses the sorting order of the elements.
# Syntax
# list.reverse() No parameters

# Reverse the order of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

# %% sort()	Sorts the list
# The sort() method sorts the list ascending by default.
# You can also make a function to decide the sorting criteria(s).
# Syntax
# list.sort(reverse=True|False, key=myFunc)
# Parameter Values
# Parameter 	Description
# reverse 	Optional. reverse=True will sort the list descending. Default is reverse=False
# key 	Optional. A function to specify the sorting criteria(s)

# Sort the list descending:
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)
# Sort the list alphabetically:
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
# %%list()
# It is also possible to use the list() constructor to make a new list.
# Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)

# %%del keyword
# The del keyword can also delete the list completely:
thislist = ["apple", "banana", "cherry"]
del thislist

# The del keyword removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]

print(thislist)

# %%Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
# Example
# Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# %%
# LIST key points
# when we do the item assignment of the sequence with slicing then make sure you 
# use the correct iterable item to replace the value.
# like  s=[1,2,3,4] if s[0:4:2]=[123] then it will error as we are trying to replace
# two items from list but only item has been passed to assignement.
# also if slicing then make sure do not use pure int/float/complex as they are not 
# iterable items

# test code
# when you write a code  make sure its conditions follows for all set of data
# 1. for all met conditions 
# 2. for more then condition value like more then defined values
# 3. empty values like below it mostly works for all set of data to remove the values
# from list
data = [1, 2, 100, 101, 150, 200, 201, 299, 300, 301]
# data=[100,101,150,200,201,299,300,301]
# data=[1,2,100,101,150,200,201,299]
# data=[101,103,1000,1001,1003]
# data=[1,2,100,101,150,200,201,299,300,301]

min_value = 100
max_value = 300
A = None  # for debugging only
for index in range(len(data) - 1, -1, -1):
    # if we are removing values from sequence with for loop then make sure you 
    # understood how it work.
    # in list when we use for loop it will only move forward , when we remove the items
    # from sequence
    # then at that time sequence index /length also reduced and adjacent values which
    # needs to remove
    # wont remove as they occupy the index vale of the removed item like [1,2,100,200,300] 
    # if we removed
    # 1 then 2 wont shows up in loop as loop only move forward    A=data[index] # for debugging
    if data[index] > max_value or data[index] < min_value:
        print(index, data)
        del data[index]
print(data)
# for ordered list/sequence
data = [1, 2, 100, 101, 150, 200, 201, 299, 300, 301]
# data=[100,101,150,200,201,299,300,301]
# data=[1,2,100,101,150,200,201,299]
# data=[101,103,1000,1001,1003]
# data=[1,2,100,101,150,200,201,299,300,301,302]

min_v = 100
max_v = 300
for value in data:
    if value > max_v or value < min_v:
        data.remove(value)
        # o/p will be [2,100,101,150,200,201,299,300,302] As 2 and 302 occupy the index position
        # of 1 and 301

stop = 0
for index, value in enumerate(data):
    if value > min_v:
        stop = index
        break
del data[:stop]

start = 0
for index, value in enumerate(data):  # this function will cause the issue as if conditon dont
    # statisfy then start remains 0 and del will run on all the list
    # to overcome this we can use backward indexing
    # for index in range(len(data)-1,-1,-1):
    #   if data[index] < max_v:
    #     start=index+1
    #     break
    if value > max_v:
        start = index + 1
        break
del data[start:]
print(data)
# %%
# split method (its string method but canbe useto create  lists)
# it creates lists from string  # .split() .. ()> can contain the arguments
# () > by default to whitespace > whitespace includes things like tabs ,newline,space
print('9,233,344,455,666'.split())  # it will print whole as list only one item as no space in item
# o/p ['9,233,344,455,666']
print(
    '9,233,344,455,666'.split(',', 1))  # it will print two items one '9,' and other whole string as after 9 space found
# o/p ['9', '233,344,455,666']
# 1st method
A = '9,233,344,455,666'.split(',')
B = []
for item in A:
    B.append(int(item))
print(A)  # ['9', '233', '344', '455', '666']
print(B)  # [9, 233, 344, 455, 666]

# 2nd method
A = '9,233,344,455,666'.split(',')
for index, item in enumerate(A):
    A[index] = int(item)
print(A)  # [9, 233, 344, 455, 666]
# 3rd method
A = '9,233,344,455,666'.split(',')
for index in range(len(A)):
    A[index] = int(A[index])
print(A)  # [9, 233, 344, 455, 666]
print(tuple(A))  # (9, 233, 344, 455, 666)
