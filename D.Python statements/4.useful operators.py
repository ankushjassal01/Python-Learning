#%% Enumerate functions
# it give o/p with index location value and its values. but in tuples form
#we can use tuples unpacking
index_count = 0

for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1
    
# to overcome above we can use enumerate
for letters in enumerate('abcde'):
    print(letters) # it
for index,value in enumerate('abcde'): # tuples unpacking
    print(index)
    print(value)
    print()

    
index_count = 0
for letters in 'abcde':
    print(letters[index_count])# it wil give error as letter will be a b  c d e but 
    # index is increcresing so it will give error as b[1] is not true 
    index_count += 1 # if omit this then no error in console


#%%ZIP function
# it works exactly as enumerate but it need two params
# if lists are not have same length then extra length will be ignored 
list1=[1,1,2,3]
list2=[1,2,3,4]
list3=[1]
print(list(zip(list1,list3))) ##[(1, 1)]
print(list(zip(list1)))  # it can work with one param too but it give o/p  in tuples where
# one is param1 value and separeted by comma, like [(1,), (1,), (2,), (3,)]
a= (list(zip(list1))[1])
print(len(a)) # 1

#%% in  operator
# We've already seen the in keyword during the for loop, but we can also use it to 
# quickly check if an object is in a list
# it give true or false result. wether it is in the list/str/dict etc
print(1 in [1,2,3])
print(1 in 1) #: argument of type 'int' is not iterable
#%% min or max function 
# works with str/list/tuples/dict
list1=[1,2,3,4]
print(min(list1))
print(max(list1))
list1='class'
print(min(list1))
print(max(list1))
print()
list1={'a':1,'b':2} # in dict only keys are going to print with min until indexing used
print(min(list1))
print(max(list1))
list1=(1,3)
list1=(1,3,'class') # it should all str or all int in list/tuples.
print(min(list1))
print(max(list1))

#%% random library
# its built in random library. it have multiple built functions
# to use thos follow below syntax . use tab to get functions list
from random import randint
# dont work on str as TypeError: 'str' object does not support item assignment
# a='class'
a= ['class',1,2,3,4]
print(shuffle(a)) # it give none type when printed as it dont give any o/p
print(a) #['class', 2, 3, 1]
print(randint(0,100))

#%% input function
# it take input from the user in console
# but it give o/p in string only. so we can covert them into int/float/list
a=input('what is your full name : ')
print(a)