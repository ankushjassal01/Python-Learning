# its unique way to quicky creating a list with python
# In addition to sequence operations and list methods, Python includes a more advanced 
# operation called a list comprehension.
# List comprehensions allow us to build out lists using a different notation. You can think
#  of it as essentially a one line for loop built inside of brackets. For a simple examp.
# Grab every letter in string
lst = [x for x in 'word']
print(lst)
print()
# This is the basic idea of a list comprehension. If you're familiar with mathematical notation 
# this format should feel familiar for example: x^2 : x in { 0,1,2...10 }
# Let's see a few more examples of list comprehensions in Python:
# Square numbers in range and turn into list
lst = [x**2 for x in range(0,11)]
print(lst)
print()
# Let's see how to add in if statements:
# Check for even numbers in a range
lst = [x for x in range(11) if x % 2 == 0]
print(lst)
print()
# Can also do more complicated arithmetic:
# Convert Celsius to Fahrenheit
celsius = [0,10,20.1,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius ]
print(fahrenheit)
print()
# We can also perform nested list comprehensions, for example:
lst = [ x**2 for x in [x**2 for x in range(11)]]
print(lst)
print()

#%% if else
r=['{} is even'.format(x) if x%2==0 else '{} is odd'.format(x) for x in range(10)]
print(r)

#%% nested for 
li=[]
for x in range(5): # here x will multiple with each y as its in loop .
    for y in range(5): # here each y will multiple with one x multiple times until loop end.
        li.append(x*y)
print(li)

for x in 'y': #y will multiple multiple time first with 0 then 1 and 2 and 3 and 4 .
    for y in range(5): # o/p will ..y yy yyy yyyy
        print(x*y)



print('an'*0)

#%%
# Use for, .split(), and if to create a Statement that will print out words that start with 's':
# r=[ i if i%3 == 0 for i in range(1,51)] # this is wrong format as in list comp alone if dont be 
# use ahead of for . it will always behind/after the for 
r=[ i for i in range(1,51) if i%3 == 0 ] 
print(r)

#%%
#Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'

for x in st.split():
        if len(x)%2 ==00:
            print('Even length: '+x)
        else:
            print('odd length: '+x)

#%%
#vWrite a program that prints the integers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number, 
# and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1, 101):
    if i%3==0 and i%5==0:
        print(str(i) +'=FizzBuzz')   
    elif i%5==0:
        print(str(i)+'=Buzz')
    elif i%3==0:
        print(str(i)+'=Fizz')
    else :
        print(i)

#%%
# Use List Comprehension to create a list of the first letters of every word in 
# the string below:
st = 'Create a list of the first letters of every word in this string'
result=[ x[0] for x in st.split()]
print(result)