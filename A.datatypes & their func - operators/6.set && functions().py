#%%SETS
#UNORDERED collection of UNIQUE VALUES
#Repeatable Vlaues will not count in print
#ITEM ASSIGNEMENT wont work
#SLICING/INDEXING/CONCATINATION wont work. 
#inclosed inside {} mostly but it wont become dict
# set() is used when we need to Assign different variable/objects but at a time only
# we can pass multiple values by list  in set() then it works 
# set can contain the multiple datatypes
# set{} will not work .its give error
# cannot add pure list inside set{}  or set(). it will give error.
#Set=set(['value',[1,2]]) #[1,2] part will give error.A={['val']} #also error
Set={1,2,3,'class'} 
print(Set)
#Set={['class']} ## error of hashable type:list
#below examples only with the set() function... must remeber that. with {} it dont give that.
#but
# with set .if inclosed list then it will passed same is it like a list object
Set=set(['class']) 
print(Set)
# it will take as string arguments/make it as single objects and 
#remove the repeated one and add them in Set values
print()
Set=set('class') 
print(Set)

S={'class'} # direct giving the value to set curly braces. 
print(S) #{'class'}
S={'class','values',1}  #with multiple values
print(S) #{'values', 'class', 1}
S=set({'class'}) # set with set curly braces values. it give same result and no parsing
print(S) #{'class'}
A='ankush jassal'
S=set(A) #if passed as variable then  parsing will be done and repeated values will be removed
print(S) #{'l', 'a', ' ', 'k', 'n', 'u', 'j', 'h', 's'}
S=set({A}) # if inclosed inside curly then it will not parse.
print(S) #{'ankush jassal'}
S=set([A]) #if inclosed inside list then it will not parse.
print(S) #{'ankush jassal'}
S=set('class')  # if value passed like this then it will be parsed and duplicate removed 
print(S) #{'a', 's', 'l', 'c'}
S=set({'class','values',1}) # it will not parsed and give value exactly like [] 
print(S) # {'values', 'class', 1}
S=set(['class','values',1]) # will not parsed and give value correctly with curly bracses
print(S) # {'values', 'class', 1}
S=set('class','values',1) # multiple values without curly or square brakets
print(S) # error
#%%BOOLEANS
#only True or False . exact same order( not true or TRUE)
#deals with logics and control flow
#used with comparision operator
A='Anksuh'
B='ANKUSH'
print(A == B) # false
print()

#%%we can assigne None value to any object if dont want to assign it value now
A=None  # not NONE or none only None
print(A)
print(type(A))

#%%
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

print(l_one[2][0] >= l_two[2]['k1'])

myset1=(1,2,3,'on')
print(myset1)
print(type(myset1))
print()
myset2 =('pythonhub','instagram')
print(myset2)
print(type(myset2))
print()
myset=myset1 + myset2
print(myset)
print(type(myset))
print()
myset=set(myset)
print(myset)
print(type(myset))



#######################  SET METHODS BELOW  #######################################
#######################                     #######################################
#%% Get the Length of a Set
# To determine how many items a set has, use the len() method.
# Example

# Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}

print(len(thisset)) 

#%% add()	Adds an element to the set
# The add() method adds an element to the set.
# If the element already exists, the add() method does not add the element.
# Syntax
# set.add(elmnt)
# Parameter Values
# Parameter 	Description
# elmnt 	Required. The element to add to the set

# Add an element to the fruits set:
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits) 

#Try to add an element that already exists:
fruits = {"apple", "banana", "cherry"}
fruits.add("apple") #it will not add/change anything nor it give error as set are unique
print(fruits) 

#%% clear()	Removes all the elements from the set
# The clear() method removes all elements in a set.
# Syntax
# set.clear()
# Parameter Values
# No parameters

# Remove all elements from the fruits set:
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits) 

#%% copy()	Returns a copy of the set
# the copy() method copies the set.
# Syntax
# set.copy() No parameters

# Copy the fruits set:
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()  # order might not be same of o/p as sets are unordered
print(x) 

#%% difference()	Returns a set containing the difference between two or more sets
# The difference() method returns a set that contains the difference between two sets.
# Meaning: The returned set contains items that exist only in the first set(unique values), and not in both sets.
# Syntax
# set.difference(set)
# Parameter Values
# Parameter 	Description
# set 	Required. The set to check for differences in

#Reverse the first example. Return a set that contains the items that only exist in set y, and not in 
# set x:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=y.difference(x)#am putting method on Y so Y values will be returned which are not in X
print(z) # the o/p of difference() need to be in another variable becaue it do not alter the 
         #original value

#Return a set that contains the items that only exist in set x, and not in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z) 

#%% difference_update()	Removes the items in this set that are also included in another, 
# specified set

# The difference_update() method removes the items that exist in both sets.
# The difference_update() method is different from the difference() method, because 
# the difference() method returns a new set, without the unwanted ( similar) items, and the 
# difference_update() method removes the unwanted( similar) items from the original set.
# Syntax
# set.difference_update(set)
# Parameter Values
# Parameter 	Description
# set 	Required. The set to check for differences in

# Remove the items that exist in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y) # method on X
print(x) # {'cherry', 'banana'}
print(y) # {'apple', 'microsoft', 'google'}
y.difference_update(x) # it does not update anything as X already have unique values now 
print(y) # {'apple', 'microsoft', 'google'}
y.difference_update(x)  # it does not update anything as X already have unique values now
print(y) # {'apple', 'microsoft', 'google'}

#%% discard()	Remove the specified item
# The discard() method removes the specified item from the set.
# This method is different from the remove() method, because the remove() method 
# will raise an error if the specified item does not exist, and the discard() method will not.
# Syntax
# set.discard(value)
# Parameter Values
# Parameter 	Description
# value 	Required. The item to search for, and remove

# Remove "banana" from the set:
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits) 
fruits.discard("cherr") # it wont return erro it just return the out of set
print(fruits) 

#%% intersection()	Returns a set, that is the intersection of two other sets
# The intersection() method returns a set that contains the similarity between two or more sets.
# Meaning: The returned set contains only items that exist in both sets, or in all sets if the comparison is done with more than two sets.
# Syntax
# set.intersection(set1, set2 ... etc)
# Parameter Values
# Parameter 	Description
# set1 	Required. The set to search for equal items in
# set2 	Optional. The other set to search for equal items in.
# You can compare as many sets you like.
# Separate the sets with a comma
# Compare 3 sets, and return a set with items that is present in all 3 sets:
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z) 
print(result) # the o/p of difference() need to be in another variable becaue it do not alter the original value

#Return a set that contains the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z) 

#%% intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# The intersection_update() method removes the items that is not present in both sets (or in all 
#  if the 
#comparison is done between more than two sets).
# The intersection_update() method is different from the intersection() method, because the 
# intersection() method 
#returns a new set, without the unwanted (non  similar) items, and the intersection_update() method removes the
#  unwanted (non  similar) items from the original set.
# Syntax
# set.intersection_update(set1, set2 ... etc)
# Parameter Values
# Parameter 	Description
# set1 	Required. The set to search for equal items in
# set2 	Optional. The other set to search for equal items in.
# You can compare as many sets you like.
# Separate the sets with a comma

# Compare 3 sets, and return a set with items that is present in all 3 sets:
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y, z)
print(x) 

#Remove the items that is not present in both x and y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x) 

#%% isdisjoint()	Returns whether two sets have a intersection or not
# The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
# Syntax
# set.isdisjoint(set)
# Parameter Values
# Parameter 	Description
# set 	Required. The set to search for equal items in

# What if no items are present in both sets?
#Return False if one ore more items are present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y)
print(z) 

#Return True if no items in set x is present in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z) 

#%% issubset()	Returns whether another set contains this set or not
# The issubset() method returns True if all items in the set exists in the specified set, otherwise it retuns False.
# Syntax
# set.issubset(set)
# Parameter Values
# Parameter 	Description
# set 	Required. The set to search for equal items in

#What if not all items are present in the specified set?
#Return False if not all items in set x are present in set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y)
print(z) 
z = y.issubset(y) #true as set is subset of itself
print(z) 
#Return True if all items set x are present in set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z) 

#%% issuperset()	Returns whether this set contains another set or not
# The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it retuns False.
# Syntax
# set.issuperset(set)
# Parameter Values
# Parameter 	Description
# set 	Required. The set to search for equal items in

# What if not all items are present in the specified set?
# Return False if not all items in set y are present in set x:
x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z) 
z = y.issuperset(y)
print(z) 
z = y.issuperset(x)
print(z) 

#Return True if all items set y are present in set x:
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y) ## item of set y in x
print(z) 
z = y.issuperset(x) ## item of set x in y
print(z) 

#%% pop()	Removes an element from the set
# The pop() method removes a random item from the set.
# This method returns the removed item.
# Syntax
# set.pop()
# Parameter Values
# No parameter values.

# Return the removed element:
fruits = {"apple", "banana", "cherry"}
x = fruits.pop()
print(x) 
x = fruits.pop()
print(x) 

# Note: The pop() method returns removed value.

# Remove a random item from the set:
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits) 
fruits.pop()
print(fruits) 

#%% remove()	Removes the specified element
# The remove() method removes the specified element from the set.
# This method is different from the discard() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.
# Syntax
# set.remove(item)
# Parameter Values
# Parameter 	Description
# item 	Required. The item to search for, and remove

# Remove "banana" from the set:
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits) 

fruits.remove("banana")
print(fruits) 
#%% symmetric_difference()	Returns a set with the symmetric differences of two sets
# The symmetric_difference() method returns a set that contains all items from both set, but not the 
# items that are present in both sets.
# Meaning: The returned set contains a mix of items that are not present in both sets.
# Syntax
# set.symmetric_difference(set)
# Parameter Values
# Parameter 	Description
# set 	Required. The set to check for matches in

# Return a set that contains all items from both sets, except items that are present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z) 

#%% symmetric_difference_update()	inserts the symmetric differences from this set and another
# The symmetric_difference_update() method updates the original set by removing items 
# that are present in both sets,and inserting the other items.
# Syntax
# set.symmetric_difference_update(set)
# Parameter Values
# Parameter 	Description
# set 	Required. The set to check for matches in

# Remove the items that are present in both sets, AND insert the items that is not present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x) 

#%% union()	Return a set containing the union of sets
# The union() method returns a set that contains all items from the original set, and all items from the
# specified sets.You can specify as many sets you want, separated by commas.
# If an item is present in more than one set, the result will contain only one appearance of this item.
# Syntax
# set.union(set1, set2...)
# Parameter Values
# Parameter 	Description
# set1 	Required. The set to unify with
# set2 	Optional. The other set to unify with.
# You can compare as many sets as you like.
# Separate each set with a comma

# Unify more than 2 sets:
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z)
print(result) 

#Return a set that contains all items from both sets, duplicates are excluded:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z) 

#%% update()	Update the set with the union of this set and others
# The update() method updates the current set, by adding items from another set
# If an item is present in both sets, only one appearance of this item will be present in the updated set.
# Syntax
# set.update(set)
# Parameter Values
# Parameter 	Description
# set 	Required. The set insert into the current set

# Insert the items from set y into set x:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x) 

#Note: Both union() and update() will exclude any duplicate items.
#Note: Sets are unordered, so when using the pop() method, you will not know which item that gets removed.
#Note: If the item to remove does not exist, discard() will NOT raise an error.
#Note: If the item to remove does not exist, remove() will raise an error.
#NOTE: Once a set is created, you cannot change its items, but you can add new items.

