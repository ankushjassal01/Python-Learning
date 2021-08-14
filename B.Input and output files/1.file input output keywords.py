# read file from directory
# created files in directory where scripting working .check console for the 
# run file/wdir. it show the path

myfile = open('file.txt')
print(myfile)
# gives error as no such file is there in directory
# FileNotFoundError: [Errno 2] No such file or directory: 'myfiles.txt'
# myfile1=open('myfiles.txt')

# to read the file data.in juypter or other IDE it will print as in /n for new line
print(myfile.read())

# below functions is used to read the file again. as when you run the read()
# it will move the cursor to end of line in o/p. to reset it we need to use the
# seek(0).0 is for total reset. if want to see in b/w then put the length of
# characters which you want to remove. like myfile.seek(25) print from 2nd line
# it skip the length from the read() 
myfile.seek(25)

print(myfile.read())
myfile.seek(0)  # always need to to cursor the line to top of file lines
print()

# gives the LIST [] and  each line will be objects
print(myfile.readlines())

# to open the file in the different location the its pwd
# myfile=open("c:\\USERS\\iphone\\My Python Learning\\MYFILE.txt")
# to close the file as if we want to delete then python will say its already in use
# myfile.close

# %% it will print the new file as myfile.txt dont exist in file path
# it will write the file in path with the given txt.(only stings can be written)
with open ('myfile.txt', mode='w+') as B:
  B.write('\nthirty five s')

with open ('file.txt', mode='r') as B:
    # B.write('\nthirty five s')
    print(B.read())  
# %% append the file by mode a. to apend the file we first need to open it by read mode
with open ('file.txt',mode ='a') as A:
    A.write('/n this is third line')
   
with open ('myfile.txt', mode='a') as A:
    A.write('\nwritten value above is thirty five') # print(A.read()) wont work with append files

# %% used to read and write to file. it does not overwrite the file
with open ('myfile.txt', mode='r+') as A:
    A.write('a')
    print(A.readline())

# %% used to write and read the file. can overwrite the files.
# it directly make the file overwrite  if used. written data will be overwrite
with open('myfile.txt', mode='w+') as A:
    A.write('this is first line')
    print(A.readlines()) # alone used with above mode then it will make file size 0.vanish
    
# %% myfile=open('myfile.txt')
myfile.close()