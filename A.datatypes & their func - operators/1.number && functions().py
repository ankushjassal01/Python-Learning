# Numbers
# Int Float complex
# int are without decimal 1, 100,1000
# float with decimal 1.1, 100.5, 1111.5
# complex are with non real number 3 +5j

# Basic Arithmetic
# Addition
print(2+1) #3
# Subtraction
print(2-1) # 1
# Multiplication
print(2*2 ) #4
# Division
print(7/4) #1.75
# Floor Division
print(7//4) # 1
print(4.5//2) # 2.0 # if float floor division then answer will be in float
print(4.5//3) # 1.0
#So what if we just want the remainder after division?
# Modulo
print(7%4) #3 ..4 goes into 7 once, with a remainder of 3. 
           # % operator returns the remainder after division.
# Powers
print(2**3) # 8
# Can also do roots this way
print(4**0.5) # for square root  2.0
# Order of Operations followed in Python
print(2 + 10 * 10 + 3) # 105
# Can use parentheses to specify orders
print((2+10) * (10+3)) # 156

# Let's create an object called "a" and assign it the number 5
a = 5
print(a)
# Adding the objects
a=a+a # alone a+a wont work until it bind to another object.like here a
print(a)
# Reassignment
a = 10
print(a)
# precedence
# here like bodmas in python order of arthmatic opertaion decide by its 
# order of  precedence

#%%conversion functions()
#int()- convert the variable value to int
x='12'
y=1.2
z=1j #TypeError: can't convert complex to int
i='xc' # will not work
print(int(x)) #12
print(int(y)) #1
print(int(i)) #ValueError: invalid literal for int() with base 10: 'xc'
print(int(z)) # complex cannot convert to int() error


#%%float() - convert the variable value to float
x='12'
y=1.2
i='xc' # will not work
z=1j #TypeError: can't convert complex to float
print(float(x)) #12.0
print(float(y)) #1.2
print(float(i)) #ValueError: could not convert string to float: 'xc'
print(float(z)) # complex cannot convert to float() error

#%%complex()-convert the variable value to complex
x='12'
y=1.2
z=1j 
i='xc' # will not work
print(complex(x)) #(12+0j)
print(complex(y)) #(1.2+0j)
print(complex(z)) #1j
print(complex(i)) #ValueError: complex() arg is a malformed string
# no error for any type

#%%OTHER FUNCTIONS()
#RANDOM()-PYTHON DONT HAVE RANDOM FUNCTION BUT HAVE BUILT IN MODULE SO
#WE NEED IMPORT THE RANDOM MODULE AND PUT THAT IN LOOP OR VARIABLE
import random
print(random.randrange(1,10))
A=123
print(A.as_integer_ratio()) #Signature: B.as_integer_ratio() 
#Docstring:Return integer ratio
print(A.bit_length()) #Signature: A.bit_length()
#Docstring:Number of bits necessary to represent self in binary
print(A.conjugate())#Docstring: Returns self,the complex conjugate of any int.
#Type:  builtin_function_or_method
print(A.from_bytes(bytes, 'little')) #Signature: A.from_bytes(bytes, byteorder, *, signed=False)
#Docstring:Return the integer represented by the given array of bytes.