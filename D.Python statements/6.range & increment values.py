#%% range function
# syntax range(1st param, 2nd param*, 3rd param*)
# 1st param is mandatory .. should not be string/float/list/dict range('class')
# only work with pure integers
# 2nd param is optional
# 3rd param is option . its difference or stpe size.
print(range(1,9,3))#it will not use alone most of time as it is generator and 
                    # it will print same value
# generator is special function the generate information instead of saving it in memeory
print(list(range(1,9,3)))
for i in range(1,9,3):
    print(i) # 1 4 7 as o/p start with 1 as mentioned above
    
# range()
# range produces a range of numbers- from the starting value , up to but not including 
# the end value
# range(1,5) range(start point, end point, step point( stpe need start mandatory) )
# end pint is mandatory, start is optional 
for i in range(1,5):
    print(i) # it will start from 1 and print till 4, not include 5
print()
print(i)  #  this will print the last value of loop

print()
# without start value.. default is 0
for i in range(2):
    print(i) # it will print from 0 to 4 , not include the 5
print()
print(i) #  this will print the last value of loop
print()
# with step point 
for i in range(0,5,2):
    print(i)
print()
for i in range (2,4):# it will print because start is mentioned and no step there 
    print(i)
print() 
# we can count 2 as step here too and also end point. here with step no start mentioned
# also if 4 is start point then there is no negative step point mentioned 
for i in range (4,2): 
    print(i)
#%% with negative step
# it will print the o/p in decrment manner. it will display values to lowest end point
# here start must be more then end point and without start it wont work
for i in range(5,-2): # wont display any value. no start mentioned
    print(i)
# wont display anything because start is less end point with negative step
for i in range(0,5,-2):
    print(i)
# it will print as negative step and start is more then end
a=[]
for i in range(6,2,-2): # o/p will be 6,4 . 2 will be neglected as stop is 2
    print(a.append(i))
    print(a)
print(a)
#%%
a=[1,2,3,4,5,6]
b=4
for i in range(len(a)):
    if a[i] in a:
        f={i:a[i]}
        #a.append(f) # it will append the dict in list with index . it indent per if block
    #a.append(f) # same will be done in this although this under indent of for block
a.append(f) # no indent so it wil take the final value of for loop and append in list
print(a) # print the final list value
print('found at index pos {}'.format(a)) # list value in string
