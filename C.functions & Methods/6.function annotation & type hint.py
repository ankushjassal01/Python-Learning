# function annotation and type hint
# function annotation
# it helpful to determine the data type of params and return value
# if we used this then there is no need to write the datatype of param in docstring or anything about param in docstring
# to writ eth function annotation we follow below way to initialize them
# with parameter_name: datatype and once parenthesis closed then we write the return value datatype like -> int
# where we can add float and int both , there we can mark it as float per PEP 8 guideline
# these annotation is only for reference and make our life easy and prevent us to gave the wrong arguments to function
# to just display a warning that you are using wrong datatype but it  does not prevent us to type it and run
# like if int is required then we can write float too . it do not gave error and func work if no error in code .
def fibonacci(integer: int) -> int:
    """fibonacci function to gave the nth fibonacci number, for positive range of integers"""
    if integer < 0:  # check for negative integers
        raise ValueError('Negative integer: Negative Integer(-1,-2,-3...-nth) wont have fibonacci series')
    else:
        if 0 <= integer <= 1:
            return integer
        else:
            a = 0  # initial 1st value
            b = 1  # initial 2nd  value
            output = None  # defined the output as None
            for i in range(integer + 1):
                output = a + b
                a = b  # assign value of 'b' to 'a' object
                b = output  # assign value of 'output' to 'b' object
            return output  # must use print to call the function & get the return value.remember return in indent of for


print(fibonacci(5))  # gives 13
fibonacci(5)  # nothing
for f in range(6):  # for range of integer
    # calling fibonacci function in print for each value of f.
    print(f, fibonacci(f))

# %% Type Hint
# as per tutor we dont use much in code as they are not of much use and python is dynamically type language.
# if our job company required that in code documentation then we have to write it as per them.

