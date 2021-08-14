#%%DICT
#UNORDERED mapping of objects
#inclosed inside {}
#uses{Key : Value} pairs 
#does not support INDEXING AND SLICING directly
# TO overcome this we can call it with keys or key value indexing  like :A['a'] or A['a'][2]
#ITEM ASIGNEMENT supported
# assign new value to existing key : A['keyname']='newvalue'
# does not support CONCATINATION of any type
# tup={'a':1} ===tup=tup + {'b':2}  TypeError: unsupported operand type(s) for +:'dict' and 'dict'
# to overcome above thing >add new value to dict:A['newkey']='its value'
a={'a':1,'b':2}
a['a']=a['a']+1 # it works as key 'a' become 2 due to dict key value 
                # datatype is int and int+int works
# a['a']=a['a']+'str' # this wont work as a['a'] is int but int+str wont work
print(a['a'])
a['c']=3 # it add new key in defined dictionary
a['a']=5 # item assignment  by changing values
print(a)
#INDEXING/concatination WORKS WITH RESPECT TO THE DATATYPE IT HAVE, Same with it methods
a={'a':'class'}
a['a'].upper() # dict[key][itsvalue].datatypemethod()
print(a['a'].upper())
print(a)
#IF WE WANT TO CHECK THE DATA INSIDE DIFFERENT DATATYPE THEN ::
    # a={'a':[1,(1,2)]}
    # write the dict object name like a it give value {'a':[1,(1,2)]}
    #then write its defined key like a['a'] it gave [1,(1,2)] #  list
    # then write its index datatype index value like a['a'][1] it gave (1,2)#  tuple
    # it you write a['a'][1] [1]then it gave 2#  int
# write CONTAINS THE DICT THEN FIRST write INDEX WORKS THEN TO CHECK DICT KEY
#IF THEY KEY CONTAIN LIST OR SOMEELSE THEN ITS INDEX OR KEY ACCORDING TO DATA IT HAVE
#SAME FOR FUCNCTIONS. IF THAT FUNCTION DONT WORK AT THAT DATATYPE INDEX THEN IT SHOULD NOT
#BE CALLED
#due to UNRODERED , we cannot defined its order. python will give its order differently on compile
#If keys repeated then 2nd will be picked if more then 2 then last one will be picked
Dict={"a":[1,2,'cls',{'a':(1,'cls')}],"b":{"a":{"b":(1,'cls')}},"c":(1,2)}
A={'a':1,"a":2,"a":'class'}
print(A)
#print(A={'a':1,"a":2,"a":'class'}) # connot do that
# can hold MULTIPLE DATATYPES
#to counter the INDEXING AND SLICING in dict we can directly change the value
#by its key value name .
print()
A['a']=1
print(A)
print(A['a'])# to print the value of 'a'

print()
A={"a":'class'}
print(A['a'])
print(type(A['a']))
print()
print(A)
print(type(A))
print()

print(A['a'][2])# nested INDEXING by starting with key values
print(type(A['a'][2]))


#%%The del keyword can also delete the dictionary completely:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists. 

# %% Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
# Example

# Check if "model" is present in the dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") 
  
# Dictionary Length
# To determine how many items (key-value pairs) a dictionary has, use the len() function.
# Example

# Print the number of items in the dictionary:
print(len(thisdict)) 

#%% The dict() Constructor
# It is also possible to use the dict() constructor to make a new dictionary:
# Example
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

#%%clear()	Removes all the elements from the dictionary
# The clear() method removes all the elements from a dictionary.
# Syntax
# dictionary.clear()
# Parameter Values
# No parameters

# Remove all elements from the car list:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
car.clear()
print(car) 

#%% copy()	Returns a copy of the dictionary
# The copy() method returns a copy of the specified dictionary.
# Syntax
# dictionary.copy()
# Parameter Values
# No parameters
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a
# reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

#Copy the car dictionary:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.copy()
print(x) 

#%% fromkeys()	Returns a dictionary with the specified keys and value
# The fromkeys() method returns a dictionary with the specified keys and the specified value.
# Syntax
# dict.fromkeys(keys, value)
# Parameter Values
# Parameter 	Description
# keys 	Required. An iterable specifying the keys of the new dictionary
# value 	Optional. The value for all keys. Default value is None

# Same example as above, but without specifying the value:
x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x) # if no valeu then None
print(thisdict)

#Create a dictionary with 3 keys, all with the value 0:
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

#%% get()	Returns the value of the specified key
# The get() method returns the value of the item with the specified key.
# Syntax
# dictionary.get(keyname, value)
# Parameter Values
# Parameter 	Description
# keyname 	Required. The keyname of the item you want to return the value from
# value 	Optional. A value to return if the specified key does not exist.
#           Default value None

# Try to return the value of an item that do not exist:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("price", 15000)
print(x) 

#Get the value of the "model" item:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x) 

#%% items()	Returns a list containing a tuple for each key value pair
# The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
# The view object will reflect any changes done to the dictionary, see example below.
# Syntax
# dictionary.items()
# Parameter Values
# No parameters

# When an item in the dictionary changes value, the view object also gets updated:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x) 

car["year"] = 2018
print(x) 

#Return the dictionary's key-value pairs:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x) 

#%% keys()	Returns a list containing the dictionary's keys
# The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
# The view object will reflect any changes done to the dictionary, see example below.
# Syntax
# dictionary.keys()
# Parameter Values
# No parameters

# When an item is added in the dictionary, the view object also gets updated:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x) 
car["color"] = "white"
print(x) 

#Return the keys:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x) 

#%% pop()	Removes the element with the specified key
# The pop() method removes the specified item from the dictionary.
# The value of the removed item is the return value of the pop() method, see example below.
# Syntax
# dictionary.pop(keyname, defaultvalue)
# Parameter Values
# Parameter 	Description
# keyname 	Required. The keyname of the item you want to remove
# defaultvalue 	Optional. A value to return if the specified key do not exist.
# If this parameter is not specified, and the no item with the specified key is found, an error is raised

# The value of the removed item is the return value of the pop() method:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.pop("model")
print(x) 
x = car.pop("model")
print(x) 
#Remove "model" from the dictionary:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("year")
print(car) 

#%% popitem()	Removes the last inserted key-value pair
# The popitem() method removes the item that was last inserted into the dictionary. In versions before 3.7, 
# the popitem() method removes a random item.
# The removed item is the return value of the popitem() method, as a tuple, see example below.
# Syntax
# dictionary.popitem()
# Parameter Values
# No parameters

# The removed item is the return value of the pop() method:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.popitem()
print(x) 

#Remove the last item from the dictionary:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem()
print(car) 

#%% setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# The setdefault() method returns the value of the item with the specified key.
# If the key does not exist, insert the key, with the specified value, see example below
# Syntax
# dictionary.setdefault(keyname, value)
# Parameter Values
# Parameter 	Description
# keyname 	Required. The keyname of the item you want to return the value from
# value 	Optional.
#           If the key exist, this parameter has no effect.
#           If the key does not exist, this value becomes the key's value
#           Default value None

#Get the value of the "color" item, if the "color" item does not exist, insert "color" with the value "white":
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "white")
print(car) 

#Get the value of the "model" item:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)
print(car) 

#%% update()	Updates the dictionary with the specified key-value pairs
# The update() method inserts the specified items to the dictionary.
# The specified items can be a dictionary, or an iterable object.
# Syntax
# dictionary.update(iterable)
# Parameter Values
# Parameter 	Description
# iterable 	A dictionary or an iterable object with key value pairs, that will be inserted to the dictionary

# Insert an item to the dictionary:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"})
print(car) 
car.update({"year": 1999}) #can also update the exitsing value
print(car)
car.update(['22']) # it need only two values either add it as string in dict(length should be 2 only) or dict like above
print(car)

#%% values()	Returns a list of all the values in the dictionary
# The values() method returns a view object. The view object contains the values of the dictionary, as a list.
# The view object will reflect any changes done to the dictionary, see example below.
# Syntax
# dictionary.values()
# Parameter Values
# No parameters

# When a values is changed in the dictionary, the view object also gets updated:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
car["year"] = 2018
print(x) 

#Return the values:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x) 
