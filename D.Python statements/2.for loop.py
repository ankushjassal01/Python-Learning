# for loops 
# FOR loop dont work with numbers but while do
# iterable object will mostly have for loop
# in python for is different then other language for loops
# in other languages like c js java for loop have starting value, ending, increment 
# value like for (i=0,i<5, i++).but in python
# iterable :: means you can iterate over object.for example you can iterate over 
# every charcter of datatype(ie string).. Iterate over every item in list , iterate
# over every key in disctionary
# syntax
my_iter ={"a":1,"b":2,"c":3} # it will give the key values to items as this is 
# how dict work in loop without any specified method for dict in for loop
for items in my_iter.values():
        print (items)
        print(type(items))
print()

for items in my_iter.items():
    print(items) # this will give the pair of key, values in tuples form
    # which we can use for unoacking as shown in below
print()
for key,value in my_iter.items():# tuples unpacking
    print(value)
# for methods of datatye we need  to use them in for statement only .. not in
#%% below code. below code might be differ as it depend for variable data type.
a=[{'a':1},1,2,3,'abc',[1,2,3]]
for ac  in a.pop():
    print(ac) # this will print 1 only but it should have print the 1 2 3
    # why it printed 1 because when ac pass 1 value to print.. it pass it to 
    # both the print command .this is how for loop work.
    # until the first value passed to for variable does not printed back the output
    # of the code written in for loop.. it will not goes to further input. it stop
    # there if any error
    print(ac.values()) # this will give error as not every element in list is dict

#%%
a=[{'a':1},1,2,3,'abc',[1,2,3]]
for ac in a.pop():
    print(ac) # now this will print 1 2 3 because in indentation block for dont
    # have the further code to execute so for will print the print(ac) again again
    # until its input ends
    
print(ac.values()) #this is outside of indentation block so it will not harm the 
# for loop code. it will give error at the end of for loop full executation 

#%% 
strings=(1,2,3,4,5,6) 
for _ in strings:
    if _ % 2 == 0:
        print('this is even :{}'. format(_))
    else:
        print('this is odd  :{}'. format(_))
        
#%% sum of numbers
strings=[1,2,3,4,5,6]
s=5
for i in strings:
    s=s+i
    print(s)
print()
print(s)
#%% we can  also put different variable in the for code . it will print if given 
# as many times for loops have the iterable objects
for si in strings: # here si not used in code below but its still needed as code will
# give o/p objects length
    print('hello')
    print(s)
print()
print(si)

#%%
A='Ankush'
for _ in A: # here we can define for loop variable like _ too as its can be of any 
# name, character but it should be same below in code if used.
    print(_)

#%%TUPLE  UNpacking 
# if tuple have different object or its in more then one pairs then we can use
# tuple unpacking
tup=(1,2,3)
for i in tup:
    print(i)
print('above script end here')   
print()

tuplist=[(1,2),(3,4),(5,6)]
print(len(tuplist))
print()
print('above script end here')   
for i in tuplist:
    print(i)# it will give the tuples pairs because that are the object inside list
print()
print('above script end here')        
for (a,b)  in tuplist:# this will do the unpacking of tuples
    print(a)#a,b are defined per length of the tuples if more then two then a,b,c etc
print()
print('above script end here')      
tuplist=[(1,2,7),(3,4,8),(5,6,9)]

for i in tuplist:
    print(i)
print()
for a,b,c in tuplist:
    print(a,b) # unpack the tuples with two values out of three

#%%
s=[1,2,3,4,5,6]
a=3
print(s.index(a))

#%%

for x in range (2,11,3):
    print(x, end ='#')
    if x==3:
        break
    else:
        x=x-1
        print(x)
print(x)
