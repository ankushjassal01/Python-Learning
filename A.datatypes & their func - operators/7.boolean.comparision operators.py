# Booleans

# For the following quiz questions, we will get a preview of comparison operators. In the table below, a=3
# and b=4.
# Operator	Description	Example
#%% == 	If the values of two operands are equal, then the condition becomes true. 	(a == b) is not true.
print(1==1) # true
print(1==2) # false
print('1'==1) # false as datatype not same
print(1==1.0) # true as float 1.0 and 1 are same
print(1==1.1) # false as 1.1 is greater then 1.0 or 1
print('bye'=='Bye') # false as string take capital letter comparision. not case sensitive 

#%% != 	If values of two operands are not equal, then condition becomes true. 	(a != b) is true.
print(1!=1) # false
print(1!=2) # true
print(1!=1.0) #false
print('1'!=1) # true
print('bye'!='Bye') #true

#%% > 	If the value of left operand is greater than the value of right operand, then condition becomes
# true. 	(a > b) is not true.
print(1>1) # false equal thing will count as false
print(1>1.0) #false equal thing will count as false
print(1>2) # false
print(2>1) #true
print('bye' > 'Bye') #true
print('Ankush ' > 'Ankush') # true length count
print(2>1>3) # false as 1>3 is not true which make whole false
print(2>1<3) #true as al condition met
# < 	If the value of left operand is less than the value of right operand, then condition becomes
# true. 	(a < b) is true.

# >= 	If the value of left operand is greater than or equal to the value of right operand,
# then condition becomes true. 	(a >= b) is not true.

# <= 	If the value of left operand is less than or equal to the value of right operand,
# then condition becomes true. 	(a <= b) is true.


#%% logical operators
# and 
# all condition should be true like in sql . 
print(1 > 2 and 2 <3 ) # false only one met
print(1 < 2 and 2 <3 ) #true both met
print()
# or 
print(1 > 2 or 2 <3 ) # true as one condition met
print(1 < 2 or 2 <3 ) # true as both met
print(1 > 2 or 2 >3 ) #false as neither met
print()
# not
print(not 1 > 2  and 2 <3)  # true as it gives opposite of what and will give
print(not 1 < 2  and 2 <3) # false 
print()
print(not 1 > 2  or 2 <3) # true no idea 
print(not 1 < 2 or 2 <3 ) # true # for OR always true with NOT . so be carefull what you use 
print(not 1 > 2 or 2 >3 ) # true 
