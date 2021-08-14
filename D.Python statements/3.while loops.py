#While loops .. These are pure LOOPS.
# will continue to execute a code block while some condition remains true
# syntax
# while some_boolean_condition:
    # do something
# else:
    # will do something
    
A=0
while A < 5:
    print(A)
    A=A+1 # last o/p will be 4 when further A called outside loop it will take A=A+1
    # so A=A+1  >>5
print()
print(A) # this will give 5 because of A+1 
A=0 # it make A again 0 and fed it to below while loop A>3 one
# while A <5:
    # print(A+1) #this will become as infinite loop.so we aware of that as 0+1 always
    # less then 5 

#%% loops keywords
# break:breaks out of the current closest enclosing loop
A='ankush'
for i in A:
    if i == 'a': # if A then continue not work as its not true
        continue  # this will continue to loop without printing below print
        # this is helpful to avoid error and if we want to ignore something in o/p
        # here a will be missing
    print(i)

A=0 
while A <5:
    print(A+1)
    break # it break the infinite loop 
print()   
A='ankush'
for i in A:
    if i == 'k': # if K then continue not work as its not true
        break  # this will break the loop and print till n .. only a and n as at k
        # it breaks or stop.
        # this is helpful to avoid into felling into infinite loop
    print(i)

A='ankush'
while len(A) <7:
    print(A) # ankush as o/p .. not as iterable like for . FOR loop dont work with numbers but while do
    break

A=[1,2,3,4,5,6]
B=4

for i in range(len(A)):
    print(A[i])
    if A[i]==B: # o/p 1 2 3 4
        break
print()
for i in range(len(A)):
    if A[i]==B: # o//p will be 1 2 3
        break
    print(A[i])

#%% continue: goes to the top of the closest enclising loop
# A='ankush'

# for i in A:
#     if i == 'a': # if A then continue not work as its not true
#         continue  # this will continue to loop without printing below print
#         # this is helpful to avoid error and if we want to ignore something in o/p
#         # here a will be missing
#     print(i)
# print()

A=[1,2,3,4,5,6]
B=4

for i in range(len(A)):
    print(A[i])
    if A[i]==B: # o/p 1 2 3 4
        continue
print()
for i in range(len(A)):
    if A[i]==B: # o//p will be 1 2 3
        continue
    print(A[i])
    
#%% pass : Does nothing at all
print()
a=[1]
for i in a:
    # comments # without any code it wilgive syntax error as python expect code
    # after loops initilization. In that case we can use pass keyword
    pass
    #pass uses when we need to pass the loop without writing any code in it
    #it is helpful when developer need to define a loop but loop code block will be 
    # written later.to save time and avoid syntax error
print(a) # this will give the [1] .