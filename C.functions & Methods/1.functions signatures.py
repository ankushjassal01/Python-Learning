# what is function:
# function is code  , its not bound to object
# it will work without param or with params too
# it run without object like func()


# what is method:
"""
its a function bound to a class
method are defined functions but it bound to the object.
it will call with obejct with dot notation. like x.method()
Method always have parentheses. and they can have parameters/arguments
if run without parentheses then it will give sytanx defination
it will not give error
"""

# function signature

# its means definition of a function
# it includes func name, the parameters that it defines
# print(*objects,sep=' ',end='\n',file=sys.stdout,flush=False)
# Not all functions have parameters, but the parentheses
# object has an asterisk before it:explanation
# that means you can provide zero or more values. we've usually(*args)
# only provided one value or none, when we wanted to print a
# blank line.
# then function can have several keyword arguments:
# Also called as named arguments
# Here print (line 14) have 4 total key arguments
# sep, end , file, flush
# usually if dont define the value to these keyword then it takes
# default values like sep have '' end have
# # print functions keyword(named arguments):
# sep=', '> this will separated the output with , and space for each
# value. this only works for multiple object print
# end=' ' > this will give the output in one line if used with
# iteration loop like FOR.it add space . if without
# space then it will give no space between output

# syntax
# def function_name('arguments if needed'):
#     code block


def a():
    b = 2 * 10
    return b


a = a()
print(a)


# %% parameters
# parameters are like placeholder for the real values that you'll pass to you function
# they are variables but they're given a value when you call the function .
# mostly coding person call it a formal parameter or arguments of function
# they are local to the function

# arguments
# arguments are value of parameters -->which we used when defining the function.
# arguments replaced the parameters when we called the function
# we called it as passing the arguments.
# if argument/parameter required then we cannot ignore it when we calling the function
def a(x, y):
    out = x * y
    return out


b = a(3,4)  # earlier i wrote a=a(3,4) which is causing issue in below for loop
# function calling as its pointing its to a variable rather then a() function
print(b)

for i in range(1, 5):
    for j in range(1, 11):
        # times = a(i,j)
        print('{} times {} is {}'.format(i, j, a(i, j)))


# debugging with parameters
# for those who programmed earlier.python arguments are ""passed by assignment""
# the behaviour is similar to ""pass by reference"", when passing a mutable object
# for immutable  objects , the behaviour is closer to ""pass by value""
# when a argument passed to function then the parameter of function get the value of the 
# arguments as defined in function parameter like a(1,2) then x=1,y=2
# these a(1,2) can be called as positional arguments as they assigned to parameters in position
# and in order they appear
# calling a function in  code
# python will go to the function code and
# when function code terminate then python return to the line where function was called and the assignment if
# required or just provide the return value


# %%
# function testing with one liner and also using datatype method ..
# also  using them in loops/conditions
def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()  # casefold  is stronger then lower().
    # return string[::-1].lower() == string.lower()


word = input('please write the word: ')
if is_palindrome(word):
    print('{} is palindrome'.format(word))
else:
    print('{} is not palindrome'.format(word))


def palindrome_Sentence(str_sentence):
    sentence = ''
    for char in str_sentence.casefold():
        if char.isalnum() == True:
            sentence += char
    # this is called as function calling another function .
    # here we gave some output of outer function to inner function(is_palindrome(string))
    # this way its easy to fix the bug as only function code block needs changes and rest automatic changes
    return is_palindrome(sentence)  # sentence after for loop become easy to use
    # return sentence[::-1] == sentence


sentence = input('please write the sentence: ')
if palindrome_Sentence(sentence):
    print('{} is palindrome'.format(sentence))
else:
    print('{} is not palindrome'.format(sentence))
