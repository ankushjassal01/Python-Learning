# IF IS NOT A LOOP ITS A CONDITION 
#if elif else condition
# only work with boolean like true or false or logical operators or comparison 
# operators... BUT not work with = as its not boolean
# if somecondition:#first condition and below is code which run if condition is true
    # somecode
# elif someconditon2: # multiple condition before else condition met 
    # somecode
# elif someconditon3: # multiple condition before else condition met 
    # somecode  
# else:   # else wont need any condition
    # somecode #
#%%
some_condition=1
if some_condition == 0: # this false so below code wont work
    some_condition=some_condition + 3
    print(some_condition) 
elif some_condition !=0: # this true as 1 !=0 so below code run
    some_condition = 0
    print(some_condition)
else: # this will not run as above condition met
    print('number is more then 0')
#%%   
some_condition=1
if some_condition == 0: # this false so below code wont work
    some_condition=some_condition + 3
    print(some_condition) 
elif some_condition < 0: # this false so below code wont work
    some_condition = 0
    print(some_condition)
else: # this will run as above both condition is not true 
    print('number is more then 0')


#%%
strings=(1,2,3,4,5,6) # this odd and even condition dont work without for as below 
# condition value is not int. so make it int we need to use the for 
for _ in strings:
    if _ % 2 == 0:
        print('this is even :{}'. format(_))
    else:
        print('this is odd  :{}'. format(_))

#%%
# if we use multiple ifs the each if will act a alone if  block and else also
# works as alone.
# so when i have value 1. it will print if conditon one also and else 
# else condition four too
a=[1,2,3,4]
for i in a:
    if i==1:
        print('one') #one
    if i==2:
        print('two') ##two
    if i==3: # when i reach to 3 it wont print else as block work as if else 
             # not alone if and else
             # here line 55 and line 59 condition act as single if else block
             # that why each time i run it print else until it reached the 
             # the i ==3 .for i<3 it print four beacause it think it as else
        print('three') ###three 
    else:
        print('four') #four ##four ####four
print(i) ##### 

# to optimize and get correct desired output always use if elif 
# elif block will run as if else block . if IF works then else wont print
a=[1,2,3,4]
for i in a:
    if i==1:
        print('one')
    elif i==2:
        print('two')
    elif i==3:
        print('three')
    else:
        print('four')
print(i)


    
    
    