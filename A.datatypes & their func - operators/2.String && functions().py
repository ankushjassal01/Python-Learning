#%%STRINGS
#ORDERED sequence of objects
#Always inside the quotes "" or ''
# are Immutable  
# if we use id function for each of string variable , it will have different value 
# each time if we change the string value
A='Jassal'
print('A id')
print(A)
print(id(A)) #47814367280 can be change if rerun after closing IDE or direct rerun
A=A+ ' J' #47814367728
print('A id again ')
print(A)
print(id(A)) #47814367408 
A='Ankush Jassal'
print('A id again')
print(A)
print(id(A))
C=A # if we change C value with another value then it do not change the A value like in List
print('C id')
print(C)
print(id(C))
C=C+'Jas'
print('c id again')
print(C)
print(id(C))
print('A id again')
print(A)
print(id(A))
B='is my Name'
print(A+B) # CONCATINATION
#support CONCATINATION of same datatyes only
##but pure str+ pure list or pure dict or pure float or pure str or pure int wont works (# its case for all the datatypes)
print(A+" "+B) # with space between two var
## escape char+quote inside quote wont work inside triple quotes
print("""A's is  \nfirstname and B's \tlastname""")
##we can use defined variable with comma to in , comma works as a space
print('my name is',A)
# its support INDEXING AND SLICING
# it does not support ITEM ASIGNEMENT
# it have its its format method .format/f string
# we can use INDEXING AND SLICING with CONCATINATION for string ITEM ASIGNEMENT
C= "J"+A[1:]
print(C)
#MULTIPLE DATATYPES  (but those will datatypes will lose its identity)
tup='[1,2]'
tup[0] or tup[1]  ## will  be'['  and '1'

# String Methods
# Python has a set of built-in methods that you can use on strings.
# Note: All string methods returns new values. They do not change the original string.

#%% capitalize()	Converts the first character to upper case
# The capitalize() method returns a string where the first character is upper case.
# string.capitalize() No parameters

# See what happens if the first character is a number:
txt = "36 is my age." # if number is then no effect. only first word wil be captialize
txt1='my name is ankush'
x = txt.capitalize()
print (x)
print(txt1.capitalize()) # do not alter the original value only give the new value
print (txt1) # above function wont affect the original value
 
#%% casefold()	Converts string into lower case
# The casefold() method returns a string where all the characters are lower case.
# This method is similar to the lower() method, but the casefold() method is stronger, 
# more aggressive, meaning that it will convert more characters into lower case, and will 
# find more matches when comparing two strings and both are converted using the casefold() method.
# string.casefold()  No parameters

# Make the string lower case:
txt = "HELLOW, And WELCOME To My World!"
x = txt.casefold()
print(x) 

#%% center()	Returns a centered string
# The center() method will center align the string, using a specified character (space is default)
# as the fill character.
# string.center(length, character) 
# Parameter 	Description
# length 	Required. The length of the returned string
# character 	Optional. The character to fill the missing space on each side. Default is " " (space)
# NO space like "" or '' and pure int/float will throw error. as only string character works
# Using the letter "O" as the padding character
txt = "banana"
# x = txt.center(20, "") # this will give error as TypeError: 
#                    The fill character must be exactly one character long
x = txt.center(20, '0') # '0' will not throw error but 0 do
print(x)
 
# Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:
txt = "banana"
x = txt.center(20)
print(x)
 
# %% count()	Returns the number of times a specified value occurs in a string
# The count() method returns the number of times a specified value appears in the string.
# string.count(value, start, end) 
# Parameter 	Description
# value 	Required. A String. The string to value to search for
# start 	Optional. An Integer. The position to start the search. Default is 0
# end 	Optional. An Integer. The position to end the search. Default is the end of the string

# Search from position 10 to 24:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x) 
X = 'mmm vvv xxx'
print(X.count('x',7,11)) # its give 3
# Return the number of times the value "apple" appears in the string:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")  # if no start then default to 0 and end is total length of string.no indexing directly works. also it give 2 as apple string repated twice.. apples and apple
print(x) 

# %% encode()	Returns an encoded version of the string
# The encode() method encodes the string, using the specified encoding. If no encoding is 
# specified, UTF-8 will be used.
# string.encode(encoding=encoding, errors=errors) 
# Parameter 	Description
# encoding 	Optional. A String specifying the encoding to use. Default is UTF-8
# errors 	Optional. A String specifying the error method. Legal values are:
#           'backslashreplace'	- uses a backslash instead of the character that could not be encoded
#           'ignore'	- ignores the characters that cannot be encoded
#           'namereplace'	- replaces the character with a text explaining the character
#           'strict'	- Default, raises an error on failure
#           'replace'	- replaces the character with a questionmark
#           'xmlcharrefreplace'	- replaces the character with an xml character

# These examples uses ascii encoding, and a character that cannot be encoded, showing the 
# result with different errors:
txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

# UTF-8 encode the string:
txt = "My name is Ståle"
x = txt.encode()
print(x) 


# %% endswith()	Returns true if the string ends with the specified value
# The endswith() method returns True if the string ends with the specified value, otherwise False.
# string.endswith(value, start, end) 
# Parameter 	Description
# value 	Required. The value to check if the string ends with
# start 	Optional. An Integer specifying at which position to start the search
# end 	Optional. An Integer specifying at which position to end the search

# Check if the string ends with the phrase "my world.":
txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x) 
print(len(txt))
# Check if position 5 to 11 ends with the phrase "my world.":
txt = "Hello, welcome to my world."
x = txt.endswith(".", 25,27)  # total string length will be end point in -1 or indexing one like 26 here
print(x)  


# Check if the string ends with a punctuation sign (.):
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x) 



# %% expandtabs()	Sets the tab size of the string
# The expandtabs() method sets the tab size to the specified number of whitespaces.
# string.expandtabs(tabsize) 
# Parameter 	Description
# tabsize 	Optional. A number specifying the tabsize. Default tabsize is 8

# See the result using different tab sizes:
txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10)) 

# Set the tab size to 2 whitespaces:
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2) # only works with string which have \t
print(x)

X='hello'
print(X)
print(X.expandtabs(5))  ## with \t it wont work

# %% find()	Searches the string for a specified value and returns the position of where it was found
# The find() method finds the first occurrence of the specified value.
# The find() method returns -1 (not index value)(means not found in string) if the value is not found.
# The find() method is almost the same as the index() method, the only difference is that the index()
# method raises an exception if the value is not found.
# string.find(value, start, end) 
# Parameter 	Description
# value 	Required. The value to search for
# start 	Optional. Where to start the search. Default is 0
# end 	Optional. Where to end the search. Default is to the end of the string

# Where in the text is the first occurrence of the letter "e"?:
txt = "Hello, welcome to my world."
x = txt.find("e")
print(x) 

# Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:
txt = "ere, welcome to my world."
x = txt.find("e",1,2)  # follows indexing rules / end point will not include here. thats why -1
print(x) 

# If the value is not found, the find() method returns -1, but the index() method will raise an exception:
txt = "Hello, welcome to my world."
print(txt.find("q"))
# print(txt.index("q"))

# Where in the text is the word "welcome"?:
txt = "Hello, welcome to my world."
x = txt.find("welcome",7,14)
print(x)
 
# %% format()	Formats specified values in a string
# The format() method formats the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}. Read more about the placeholders in the 
# Placeholder section below.
# The format() method returns the formatted string.
# string.format(value1, value2...) 
# The placeholders can be identified using named indexes {price}, numbered indexes {0}, or
#   even empty placeholders {}.

txt1 = "My name is {fname}, I'am {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'am {1}".format("John",36)
txt3 = "My name is {}, I'am {}".format("John",36) 
print(txt1)
print(txt2)
print(txt3)
# Formatting Types

# Inside the placeholders you can add a formatting type to format the result:

# :< 	
# Left aligns the result (within the available space)
# :> 	
# Right aligns the result (within the available space)
# :^ 	
# Center aligns the result (within the available space)
# := 	
# Places the sign to the left most position
# :+ 	
# Use a plus sign to indicate if the result is positive or negative
# :- 	
# Use a minus sign for negative values only
# :  	
# Use a space to insert an extra space before positive numbers (and a minus sign befor negative numbers)
# :, 	
# Use a comma as a thousand separator
# :_ 	
# Use a underscore as a thousand separator
# :b 	
# Binary format
# :c 		Converts the value into the corresponding unicode character
# :d 	
# Decimal format
# :e 	
# Scientific format, with a lower case e
# :E 	
# Scientific format, with an upper case E
# :f 	
# Fix point number format
# :F 	
# Fix point number format, in uppercase format (show inf and nan as INF and NAN)
# :g 		General format
# :G 		General format (using a upper case E for scientific notations)
# :o 	
# Octal format
# :x 	
# Hex format, lower case
# :X 	
# Hex format, upper case
# :n 		Number format
# :% 	
# Percentage format

# %% format_map()	Formats specified values in a string

# %% index()	Searches the string for a specified value and returns the position of where it was found
# The index() method finds the first occurrence of the specified value.
# The index() method raises an exception if the value is not found.
# The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found. (See example below)
# string.index(value, start, end) 
# Parameter 	Description
# value 	Required. The value to search for
# start 	Optional. Where to start the search. Default is 0
# end 	Optional. Where to end the search. Default is to the end of the string

# Where in the text is the first occurrence of the letter "e"?:
txt = "Hello, welcome to my world."
x = txt.index("e") # use index value return value
print(x) 

# %% isalnum()	Returns True if all characters in the string are alphanumeric
# The isalnum() method returns True if all the characters are alphanumeric, 
# meaning alphabet letter (a-z) and numbers (0-9). decimals not count
# Example of characters that are not alphanumeric: (space)!#%&? etc.
# string.isalnum()  No parameters.

# Check if all the characters in the text is alphanumeric:
txt = "Company 12" # space will cause it to be non alphanumeric
x = txt.isalnum()
print(x)
txt = "Company12" # true
x = txt.isalnum()
print(x)
Z='class'
print(Z.isalnum()) # true # all alpha also cont as alphanumeric
X='123'
print(X.isalnum()) # true # all number  also cont as alphanumeric
Y='123.4'
print(Y.isalnum()) # false# float will give false

# %% isalpha()	Returns True if all characters in the string are in the alphabet
# The isalpha() method returns True if all the characters are alphabet letters (a-z).
# Example of characters that are not alphabet letters: (space)!#%&? etc.
# string.isalpha() No parameters.

# Check if all the characters in the text is alphabetic:
txt = "Company10"
x = txt.isalpha() # mixed will give False
print(x) 

Z='class'
print(Z.isalpha()) # true
Z='class '
print(Z.isalpha()) # False space wont count as alphabets
X='123'
print(X.isalpha()) # False
Y='123.4'
print(Y.isalpha()) # False

# %%isdecimal()	Returns True if all characters in the string are decimals
# The isdecimal() method returns True if all the characters are decimals (0-9).
# This method is used on unicode objects.
# string.isdecimal()  No parameters.
a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(a.isdecimal()) # true
print(b.isdecimal()) #false
Y='123.4'
print(Y.isdecimal())  # false
X='123'
print(X.isdecimal()) # true
Z='class'
print(Z.isdecimal()) # false

# %% isdigit()	Returns True if all characters in the string are digits
# The isdigit() method returns True if all the characters are digits, otherwise False.
# Exponents, like ², are also considered to be a digit.
# string.isdigit()  No parameters.
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²  #Exponents
print(a.isdigit())
print(b.isdigit())

Y='123.4'
print(Y.isdigit())  # false decimals wont count
X='123'
print(X.isdigit()) # true
Z='class'
print(Z.isdigit()) # false # charcters wont count
 
# %% isidentifier()	Returns True if the string is an identifier
# The isidentifier() method returns True if the string is a valid identifier, 
# otherwise False.
# A string is considered a valid identifier if it only contains alphanumeric 
# letters (a-z) and (0-9), or underscores (_).  
# A valid identifier cannot start with a number, or contain any spaces.
# string.isidentifier()  #no parameters
a = "MyFolder"
b = "Demo002"
c = "2bring" # false # start with number
d = "my demo" # false # space
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

# %% islower()	Returns True if all characters in the string are lower case
# The islower() method returns True if all the characters are in lower case,otherwise False.
# Numbers, symbols and spaces are not checked, only alphabet characters.
# string.islower()  No parameters.
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"
print(a.islower())
print(b.islower())
print(c.islower()) 
# %% isnumeric()	Returns True if all characters in the string are numeric
# The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
# Exponents, like ² and ¾ are also considered to be numeric values.
# string.isnumeric()  No parameters.
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric()) 

# %% isprintable()	Returns True if all characters in the string are printable
# The isprintable() method returns True if all the characters are printable, otherwise False.
# Example of none printable character can be carriage return and line feed.
# string.isprintable()  No parameters.
txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x)
print(txt)
# %% isspace()	Returns True if all characters in the string are whitespaces
# The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.
# string.isspace() No parameters.
txt = "S   " # false as all are not whitespaces
x = txt.isspace()
print(x)

txt = "     "
x = txt.isspace()
print(x)

txt = "" # this will give false as no space 
x = txt.isspace()
print(x)
 
# %% istitle()
# Returns True if the string follows the rules of a title
# The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
# Symbols and numbers are ignored.
# string.istitle()  No parameters.
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"
print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())

# %% isupper()
# Returns True if all characters in the string are upper case
# The isupper() method returns True if all the characters are in upper case, otherwise False.
# Numbers, symbols and spaces are not checked, only alphabet characters.
# string.isupper() No parameters.
a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"
print(a.isupper())
print(b.isupper())
print(c.isupper()) 

# %% join()
# Joins the elements of an iterable to the end of the string
# The join() method takes all items in an iterable and joins them into one string.
# A string must be specified as the separator.
# string.join(iterable) 
# Parameter 	Description
# iterable 	Required. Any iterable object where all the returned values are strings
myDict = {"name": "John", "country": "Norway"}
print(myDict)
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)
# Note: When using a dictionary as an iterable, the returned values are the keys, not the values.

A='Ankush'
B= 'Jassal' # it join the B string value in A string value in such a manner that iteration of 
# string separated by the B string value
# like here A N K U S H all are separated by JASSAL.
print(B.join(A))  # AJassalnJassalkJassaluJassalsJassalh

# join method
# its string functions but can use to modify the output of list because list  
# will give output in form of Square
# brackets and inverted commas and comma like ['value','value1']
# to overcome this output it as value, value1 we can use join
# join can iterate on list and give results which we can do by writing for loop
A=['value','value1','value2']
for t in A:
    print(t , end =' ') # if we dont use print() then end = ' ' will take the output of below
    # join print and make it into one line
print()
# instead of this we can use join method
print(' | '.join(A)) # Value | Value1 | Value2
# NOTE: to use JOIN , LIST must have all the item as string datatype


# %% ljust()	Returns a left justified version of the string
# The ljust() method will left align the string, using a specified character (space is default) as the
# fill character.
# string.ljust(length, character) 
# length 	Required. The length of the returned string
# character 	Optional. A character to fill the missing space (to the right of the string). 
# Default is " " (space).
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.") 
# Note: In the result, there are actually 14 whitespaces to the right of the word banana.
txt = "banana"
x = txt.ljust(7, "A") # length should be more then the string its working on 
print(x)
x = txt.ljust(20, "") #give error as no character defined
print(x) 

# %% lower()	Converts a string into lower case
# The lower() method returns a string where all characters are lower case.
# Symbols and Numbers are ignored.
# string.lower() No parameters
txt = "Hello my FRIENDS"
x = txt.lower()
print(x) 

# %% lstrip()	Returns a left trim version of the string
# The lstrip() method removes any leading characters (space is the default leading character to remove)
# string.lstrip(characters)   
# Parameter 	Description
# characters 	Optional. A set of characters to remove as leading characters
txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")  #it remove the character from left hand side and it should be leading
# like if 'JAWAHAR' and charcter is 'A' then no effect as it started from J and if J then it will remove J only
# but if JWA then it will remove the JAWA as these are in sequence.
print(x) 
A=' JAWAHAR'
print(A.lstrip('JAW'))
#Remove spaces to the left of the string:
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite") 

# %% maketrans()	Returns a translation table to be used in translations
# The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.
# string.maketrans(x, y, z) 
# Parameter 	Description
# x 	Required. If only one parameter is specified, this has to be a dictionary describing how to perform the replace. If two or more parameters are specified, this parameter has to be a string specifying the characters you want to replace.
# y 	Optional. A string with the same length as parameter x. Each character in the first parameter will be replaced with the corresponding character in this string.
# z 	Optional. A string describing which characters to remove from the original string.

# Use a mapping table to replace many characters:
txt = "Hi Sam!";
x = "mSa";
y = "eJo";
mytable = txt.maketrans(x, y);
print(txt.translate(mytable));

# The third parameter in the mapping table describes characters that you want to remove from the string:
txt = "Good night Sam!";
x = "mSa";
y = "eJo";
z = "odnght";
mytable = txt.maketrans(x, y, z);
print(txt.translate(mytable)); 

# The maketrans() method itself returns a dictionary describing each replacement, in unicode:
txt = "Good night Sam!";
x = "mSa";
y = "eJo";
z = "odnght";
print(txt.maketrans(x, y, z)); 

# Create a mapping table, and use it in the translate() method to replace any "S" characters with a "P" character:
txt = "Hello Sam!";
mytable = txt.maketrans("S", "P");
print(txt.translate(mytable)); 

# %% partition()	Returns a tuple where the string is parted into three parts
# The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string.
# Note: This method search for the first occurrence of the specified string.
# string.partition(value) 
# Parameter 	Description
# value 	Required. The string to search for

# If the specified value is not found, the partition() method returns a tuple containing: 1 - the whole string, 2 - an empty string, 3 - an empty string:
txt = "I could eat bananas all day"
x = txt.partition("apples")
print(x) 

# Search for the word "bananas", and return a tuple with three elements:
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x) 

# %% replace()	Returns a string where a specified value is replaced with a specified value
# The replace() method replaces a specified phrase with another specified phrase.
# Note: All occurrences of the specified phrase will be replaced, if nothing else is specified.
# string.replace(oldvalue, newvalue, count) 
# Parameter 	Description
# oldvalue 	Required. The string to search for
# newvalue 	Required. The string to replace the old value with
# count 	Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences

# Replace all occurrence of the word "one":
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three")
print(x)
 
# Replace the two first occurrence of the word "one":
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x) 

# Replace the word "bananas":
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
 
# %% rfind()	Searches the string for a specified value and returns the last position of where it was found
# The rfind() method finds the last occurrence of the specified value.
# The rfind() method returns -1 if the value is not found.
# The rfind() method is almost the same as the rindex() method. See example below.
# string.rfind(value, start, end) 
# Parameter 	Description
# value 	Required. The value to search for
# start 	Optional. Where to start the search. Default is 0
# end 	Optional. Where to end the search. Default is to the end of the string

# Where in the text is the last occurrence of the letter "e"?:
txt = "Hello, welcome to my world."
x = txt.rfind("e")
print(x) 

# Where in the text is the last occurrence of the letter "e" when you only search between position 5 and 10?:
txt = "Hello, welcome to my world."
x = txt.rfind("e", 5, 10)
print(x)
 
# If the value is not found, the rfind() method returns -1, but the rindex() method will raise an exception:
txt = "Hello, welcome to my world."
print(txt.rfind("q"))
print(txt.rindex("q")) 

# where in the text is the last occurrence of the string "casa"?:
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x) 

# %% rindex()	Searches the string for a specified value and returns the last position of where it was found
# The rindex() method finds the last occurrence of the specified value.
# The rindex() method raises an exception if the value is not found.
# The rindex() method is almost the same as the rfind() method. See example below.
# string.rindex(value, start, end) 
# Parameter 	Description
# value 	Required. The value to search for
# start 	Optional. Where to start the search. Default is 0
# end 	Optional. Where to end the search. Default is to the end of the string

# Where in the text is the last occurrence of the letter "e"?:
txt = "Hello, welcome to my world."
x = txt.rindex("e")
print(x) 

# Where in the text is the last occurrence of the letter "e" when you only search between position 5 and 10?:
txt = "Hello, welcome to my world."
x = txt.rindex("e", 5, 10)
print(x) 

# If the value is not found, the rfind() method returns -1, but the rindex() method will raise an exception:
txt = "Hello, welcome to my world."
print(txt.rfind("q"))
print(txt.rindex("q")) 

# Where in the text is the last occurrence of the string "casa"?:
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x) 

# %% rjust()	Returns a right justified version of the string
# The rjust() method will right align the string, using a specified character (space is default) as the fill character.
# string.rjust(length, character) 
# Parameter Values
# Parameter 	Description
# length 	Required. The length of the returned string
# character 	Optional. A character to fill the missing space (to the left of the string). Default is " " (space).

# Using the letter "O" as the padding character:
txt = "banana"
x = txt.rjust(20, "O")
print(x) 

# Return a 20 characters long, right justified version of the word "banana":
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.") 
# Note: In the result, there are actually 14 whitespaces to the left of the word banana

# %% rpartition()	Returns a tuple where the string is parted into three parts
# The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.
# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string.
# string.rpartition(value)
# Parameter Values
# Parameter 	Description
# value 	Required. The string to search for

# If the specified value is not found, the rpartition() method returns a tuple containing: 1 - an empty string, 2 - an empty string, 3 - the whole string:
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("apples")

print(x) 

# Search for the last occurrence of the word "bananas", and return a tuple with three elements:
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x) 

# %% rsplit()	Splits the string at the specified separator, and returns a list
# The rsplit() method splits a string into a list, starting from the right.
# If no "max" is specified, this method will return the same as the split() method.
# Note: When maxsplit is specified, the list will contain the specified number of elements plus one.
# string.rsplit(separator, maxsplit)
# Parameter Values
# Parameter 	Description
# separator 	Optional. Specifies the separator to use when splitting the string. By default any
# whitespace is a separator
# maxsplit 	Optional.Specifies how many splits to do.Default value is -1, which is "all occurrences"

# Split the string into a list with maximum 2 items:
txt = "apple, banana, cherry"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)
print(x) 

# Split a string into a list, using comma, followed by a space (, ) as the separator:
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x) 

# %% rstrip()	Returns a right trim version of the string
# The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
# string.rstrip(characters)
# Parameter Values
# Parameter 	Description
# characters 	Optional. A set of characters to remove as trailing characters

# Remove the trailing characters if they are commas, s, q, or w:
txt = "ssq banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw")
print(x) 

# Remove any white spaces at the end of the string:
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite") 

# %% split()	Splits the string at the specified separator, and returns a list
# The split() method splits a string into a list.
# You can specify the separator, default separator is any whitespace.
# Note: When maxsplit is specified, the list will contain the specified number of 
# elements plus one.
# string.split(separator, maxsplit)
# Parameter Values
# Parameter 	Description
# separator 	Optional. Specifies the separator to use when splitting the string. 
# By default any whitespace is a separator
# maxsplit 	Optional. Specifies how many splits to do. Default value is -1, which 
# is "all occurrences"

# Split the string, using comma, followed by a space, as a separator:
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ",1)
print(x) 

# Use a hash character as a separator:
txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x) 

# Split the string into a list with max 2 items:
txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x) 

# %% splitlines()	Splits the string at line breaks and returns a list
# The splitlines() method splits a string into a list. The splitting is done at 
# line breaks.
# string.splitlines(keeplinebreaks)
# Parameter Values
# Parameter 	Description
# keeplinebreaks 	Optional. Specifies if the line breaks should be included 
# (True), or not (False). Default value is not (False)  
# Split the string, but keep the line breaks:
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines(True)
print(x)

# Split a string into a list where each line is a list item:
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x) 
 
# %% startswith()	Returns true if the string starts with the specified value
# The startswith() method returns True if the string starts with the specified value, otherwise False.
# string.startswith(value, start, end)
# Parameter Values
# Parameter 	Description
# value 	Required. The value to check if the string starts with
# start 	Optional. An Integer specifying at which position to start the search
# end 	Optional. An Integer specifying at which position to end the search
# Check if position 7 to 20 starts with the characters "wel":
txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x) 

# Check if the string starts with "Hello":
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x) 

# %% strip()	Returns a trimmed version of the string
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
# string.strip(characters)
# Parameter Values
# Parameter 	Description
# characters 	Optional. A set of characters to remove as leading/trailing characters

#Remove the leading and trailing characters:
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x) 

#Remove spaces at the beginning and at the end of the string:
txt = "     banana   "  
x = txt.strip()
print("of all fruits", x, "is my favorite")
# it will print only Adelai because it remove the de at the end. middle del wont be removed as strip will remove only
# from starting and ending
print("Adelaide".strip('del'))

# %% swapcase()	Swaps cases, lower case becomes upper case and vice versa
# The swapcase() method returns a string where all the upper case letters are lower case and vice versa.
# string.swapcase()
# Parameter Values
# No parameters.

# Make the lower case letters upper case and the upper case letters lower case:
txt = "Hello My Name Is PETER!!"
x = txt.swapcase()
print(x)
 
# %% title()	Converts the first character of each word to upper case
# The title() method returns a string where the first character in every word is upper case. Like a header, or a title.
# If the word contains a number or a symbol, the first letter after that will be converted to upper case.
# string.title() No parameters.
# Make the first letter in each word upper case:
txt = "Welcome to my 2nd world"
x = txt.title()
print(x) 

# Note that the first letter after a non-alphabet letter is converted into a upper case letter:
txt = "hello !b2b2b2 and 3g3g3g"
x = txt.title()
print(x) 

# Make the first letter in each word upper case:
txt = "Welcome to my world"
x = txt.title()
print(x)
 
# %% translate()	Returns a translated string
# The translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.
# Use the maketrans() method to create a mapping table.
# If a character is not specified in the dictionary/table, the character will not be replaced.
# If you use a dictionary, you must use ascii codes instead of characters.
# string.translate(table)
# Parameter Values
# Parameter 	Description
# table 	Required. Either a dictionary, or a mapping table describing how to perform the replace
# Use a mapping table to replace "S" with "P":
txt = "Hello Sam!";
mytable = txt.maketrans("S", "P");
print(txt.translate(mytable)); 

# Use a mapping table to replace many characters:
txt = "Hi Sam!";
x = "mSa";
y = "eJo";
mytable = txt.maketrans(x, y);
print(txt.translate(mytable)); 

# The third parameter in the mapping table describes characters that you want to remove from the string:
txt = "Good night Sam!";
x = "mSa";
y = "eJo";
z = "odnght";
mytable = txt.maketrans(x, y, z);
print(txt.translate(mytable)); 

# The same example as above, but using a dictionary instead of a mapping table:
txt = "Good night Sam!";
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None};
print(txt.translate(mydict)); 

# Replace any "S" characters with a "P" character:
# use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80};
txt = "Hello Sam!";
print(txt.translate(mydict));

# %% upper()	Converts a string into upper case
# The upper() method returns a string where all characters are in upper case.
#  Symbols and Numbers are ignored. 
# string.upper()
# Parameter Values
# No parameters

# Upper case the string:
txt = "Hello my friends"
x = txt.upper()
print(x) 

# %% zfill()	Fills the string with a specified number of 0 values at the beginning
# The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
# If the value of the len parameter is less than the length of the string, no filling is done.
# string.zfill(len) 
# Parameter Values
# Parameter 	Description
# len 	Required. A number specifying the position of the element you want to remove

# Fill the strings with zeros until they are 10 characters long:
a = "hello"
b = "welcome to the jungle"
c = "10.000"
print(a.zfill(10))
print(b.zfill(10)) #len is less the actual length of string so no padding of 0
print(c.zfill(10)) 

# Fill the string with zeros until it is 10 characters long:
txt = "50"
x = txt.zfill(10)
print(x) 

# %%len()
# String Length
# To get the length of a string, use the len() function.
# Example

# The len() function returns the length of a string:
a = "Hello, World!" # space also count
print(len(a))

# %%sum()
# The sum() in Python is an inbuilt function that takes an iterable and returns the sum of items in it. 
# The sum () function adds the elements of an iterable and returns the sum. The sum of numbers in the 
# list is required everywhere. 
# sum(iterable, start)
# The sum () function adds start and elements of the given iterators from left to right.
# The iterable may be Python list, tuple, set, or dictionary.

# The sum() function returns a number, the sum of all items in an iterable.
# Syntax
# sum(iterable, start)
# Parameter Values
# Parameter 	Description
# iterable 	Required. The sequence to sum
# start 	Optional. A value that is added to the return value

x=[1,2.2] # only numeric /float datatype have sum function

print(sum(x))
