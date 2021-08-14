String = 'Formatting methods'
'''
# String Formatting
# this is very useful when we are not using .format or f string methods and also want to concate different data type
# objects.So %s %d %f
# Python uses C-style string formatting to create new, formatted strings. The "%" operator is used to format a set of
# variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text
# together with "argument specifiers", special symbols like "%s" and "%d".
# Any object which is not a string can be formatted using the %s operator as well. The string which returns from the
# "repr" method of that object is formatted as the string. For example:

# Here are some basic argument specifiers you should know:
#
# %s - String (or any object with a string representation, like numbers)
#
# %d - Integers
#
# %f - Floating point numbers
#
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#
# %x/%X - Integers in hex representation (lowercase/uppercase)
'''
# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)

# You will need to write a format string which prints out the data using the following syntax: Hello John Doe.
# Your current balance is $53.44.
data = ("John", "Doe", 53.44)
format_string = "Hello"
# print("%s %s %s Your current balance is %f " % (format_string, data[0], data[1], data[2]))
print("%s %s %s Your current balance is %s " % (format_string, data[0], data[1], data[2]))
########################################################################################################################
# END keyword
# can be used to avoid the newline after the output , or endnthe output with a
# different string
a,b=0,1
while a<1000:
    print(a,end=',') # it avoid the new line like 
    #0
    #1
    #1
    a,b=b,a+b

# %%
A= 25 # defined int var
print(A)
########################################################################################################################


# %%string Str function
# print correct output as it concatinate the str+int
print('my age is '+str(A))

########################################################################################################################

# %%with .format method
A = 25
B = 2
print('my age is {}'.format(A))

# will print whole string rather then running the .format method
print('my age is {0}',format(A)) # , this can also use here ()
# it will not print the format value in define index ,rather then it will print the 
# it in after that index . like my age is {0} 25 .. this is a 6 {} class
# it will print the A value directly after string end
# either its defect or something else but we can concatinate the int variables
# in strings (check line 22 example with two variable substitution)
print('my age is ',format(A ,B))

# it will print the A value in index 0
print('my age is {0}'.format(A))

# it will print A as a because we did the keyword assignment here
print('my age is {a}'.format(a=A))

# f format method
# print(f'my age is {A}')  # f method wont work before 3.6

B ='my age is' #defined string var
print (B,format(A))

# %%string with center aligned/left aligned/right aligned width output
for i in range(1,20):
    print("number is {0:>2} its Square is {1:<3} its cube is {2:^4}".format(i,i**2,i**3))

# %% if without index also used and width assigned then it works too
# but make sure you add width at first index value too it will affect later index
# formatting
for i in range(1,20):
    print("number is {:2} its Square is {:<3}".format(i,i**2,i**3))

########################################################################################################################
# %%print the floating with width/precision
A=22/7 #pi value float assigned

print("pi value is {0:12}".format(A)) # print the default precision of 15 floats
print("pi value is {0:12f}".format(A)) # it will print the precision of 6 flots with width

# %% it will print the float precision of 12 and ignore the width as pythong ignore its if width
# is equal or same as precision and precision is important
print("pi value is {0:12.12f}".format(A)) 

# %%ignore width and print 51 float. python have limit of 51 to 53 precision only after that
# zeros will be print{0:15:12f}it start puting width start from 1 then so on
print("pi value is 15 {0:15.12f}".format(A))
print("pi value is 16 {0:16.12f}".format(A))
print("pi value is 17 {0:17.12f}".format(A))
print("pi value is {0:12.51f}".format(A))
print("pi value is {0:12.53f}".format(A))#two zeros after 51 float precision
print("pi value is {0:12.55f}".format(A))# till 51 print float the  zeros (4)

# %% precision with the width and float .. width more the float and width less then float
print("pi value is  8 {0:8.12f}".format(A))
print("pi value is  9 {0:9.12f}".format(A))
print("pi value is 10 {0:10.12f}".format(A))
print("pi value is 11 {0:11.12f}".format(A))
print("pi value is 12 {0:12.12f}".format(A))
print("pi value is 13 {0:13.12f}".format(A))
print("pi value is 14 {0:14.12f}".format(A))

# %% after the ther will no width counted if you havent reached the 15 width if precsion used with
# the float formating like{0:14:12f}just at
print("pi value is 18 {0:18.12f}".format(A))
print("pi value is 19 {0:19.12f}".format(A))
print("pi value is 20 {0:20.12f}".format(A))

# %% if width less then 9f no width count just precision of 6
print("pi value is 2  {0:2f}".format(A))
print("pi value is 3  {0:3f}".format(A))
print("pi value is 4  {0:4f}".format(A))
print("pi value is 5  {0:5f}".format(A))
print("pi value is 6  {0:6f}".format(A))
print("pi value is 7  {0:7f}".format(A))
print("pi value is 8  {0:8f}".format(A))

# %% if more then 8f and widthout width then it will start putting width starting from 1
# then 2 and so on but precsion will remain 6 only , no matter if you reach to 0:51f or 52f
print("pi value is 9  {0:9f}".format(A))
print("pi value is 10 {0:10f}".format(A))
print("pi value is 11 {0:11f}".format(A))
print("pi value is 16 {0:12f}".format(A))
print("pi value is 16 {0:13f}".format(A))
print("pi value is 16 {0:14f}".format(A))
print("pi value is 16 {0:15f}".format(A))
print("pi value is 16 {0:16f}".format(A))

###################################################################################
###################################################################################

# %% f string formatting only after 3.6 ver of python
Name = 'Ankush'
Age = 25
# print(Name +f" is {Age:,} years old")
# print(f"pi value is {22 / 7:8f}")
