# %% returns values
def years(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric() and len(temp) == 4:
            return int(temp)
        else:  # we can remove else and write code like line 35
            print('-----that is not a year.. type again-----')
        # print('-----that is not a year.. type again-----') this is not indent at if block level so if if false then print work ..
        # if if works then return terminate the while loop
        # return will terminate the while loop so no need to write the break


guess = years('write the year: ')


# %% returns None

# if function dont return anything then it return None
# return is not mention or we dont want our function to return anything
# then if we call or use our defined function then it will return the None or print the None by default
def multiply(x, y):
    result = x * y
    print(x*y)
    # return result


answer = multiply(2, 3)
print(answer)  # 6 and None  # 6 due to print
print(multiply(2, 3))  # 6 and None
multiply(2,3) # gives 6 only no None


# %% here return and print are two different things

# the function is calling directly and its PRINTING the output as expected.
# Its not returning anything so if we print it then it gives None and if assign it to another object then also None
# these are called as action type function
# where we want our function to do the action rather then return the value.Like .sort method.
def centered_text(text):
    width = 100
    if text == '*':
        print('*' * width)
    elif len(text) > (width - 4):
        print('text is more then screen size')
    else:
        print('**{}**'.format(text.center(width - 4)))


centered_text('*')
centered_text('My name is Ankush Jassal')
centered_text('I am learning Python from Udemy')
centered_text('I am out of schedule here in learning')
centered_text('My target for completion is dec 31')
centered_text('per my progress its not looking to meet even after Janurary')
centered_text('*')

print('!@#')
print(centered_text('*'))  # here first it will print the centered_text parameter output then return the None
print('!@#')
a = centered_text('*')  # first output as ******************** then  None
print(a)
