# with Return value -- Its more correct way to get the data rather then using the print value below function
# function can include the more then one return statement in single function lie below
def fibonacci(integer):
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
            for i in range(integer-1):
                output = a+b
                a = b  # assign value of 'b' to 'a' object
                b = output  # assign value of 'output' to 'b' object
            return output  # must use print to call the function & get the return value.remember return in indent of for


print(fibonacci(5))  # gives 13
fibonacci(5)  # nothing
for f in range(6):  # for range of integer
    # calling fibonacci function in print for each value of f.
    print(f, fibonacci(f))


print()


# %% with the print value
def fibonacci1(integer):
    """fibonacci function to gave the `nth` fibonacci number, for positive range of `integers`"""
    if integer < 0:  # check for negative integers
        raise ValueError('Negative integer: Negative Integer(-1,-2,-3...-nth) wont have fibonacci series')
    elif 0 <= integer <= 1:
            return integer
    else:
        a = 0  # initial 1st value
        b = 1  # initial 2nd  value
        output = 0  # defined the output as zero
        for i in range(integer):
            # below condition wont work as it will be not give correct fibonacci series data
            # if i == 0:  # to give output for 0 as 0 as o number will have the zero:
            if 0 <= i <= 1:
                output=i
                print(output)
            else:
                output = a+b
                a = b  # assign value of 'b' to 'a' object
                b = output  # assign value of 'output' to 'b' object
                print(output)  # print the output


fibonacci1(6)








