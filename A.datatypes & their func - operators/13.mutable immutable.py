#when object is described as immutable , that means it cannt be changed
# int , float, bool(true/false): a subclass of int, str , tuple, frozen set
#the documentation diesnt state that it should be object address, just that it must be
#'gurantee to be unique for this object during its lifetime
# Immuable means if  variable change then it identity get also changed but if its equal to
# another variable then that variable identity will remain same 
# if id change means object destroyed and recreated
A=True
print(id(A))  # A and B will have same identity, if B value change that does affect the A identity
              # thats why it called a immuable
              # in case of list or dict when B change A also got affected in that case. in that case
              # they will have same id through.because both are bound to same memory or value
B=A
print(id(B))
B=False
print(id(B))

print()
A=(1,2)
print(A)
print(id(A))
B=A
print(B)
print(id(B))
B+=(3,4)
print(B)
print(id(B))
print(A)
print(id(A))

#%% mutable objects
# is the one whose value can be changed
# list, dict, set, bytearray
# most of the mutable allow item assignment but Set dont
# here object dont destroyed , it just updated, its identity remain same

# list type
A=[1]
print(id(A))  # in case of list or dict when B change A also got affected in that case. in that case
              # they will have same id through.because both are bound to same memory or value
B=A
print(id(B))
B +=[2]
print(id(B))
# set type
print()
A={1,2,3,4}
print(id(A))
B=A
print(id(B))
B=B.add(5) 
print(B)
print(id(B))
print(A)
print(id(A))

# dict type
print()
A={'A':1,'B':2}
print(id(A))
B=A
print(id(B))
B['B']=5
print(B)
print(id(B))
print(A)
print(id(A))

