# append mode
# we can write data to a file in append mode ('a') too
# with append mode we can write the data to the end of the file . it do not overwrite the data in a file like write
# rather then that it write the data and let previous data in the file
# append can also create the file if it not present in file directory where you running .py file
with open('2abc.txt','a') as a:
    for i in range(1,11):
        print('{:=2} times 2 is {:=2}'.format(i, i*2),file=a)


with open('2a.txt','a') as a:
    for i in range(1,11):
        print('{:=2} times 2 is {:=2}'.format(i, i*2),file=a)

with open('append_file.txt','a') as J:
    for i in range(2,12):
        for j in range(1,13):
            print('{:=2} times {:2} is {:2}'.format(i,j ,i*j),file=J)
        print('_'*20,file=J)
    # print(J.read()) # io.UnsupportedOperation: not readable

with open('append_file.txt','r') as a:
    print(a.read())


# we can read the file which appended in read mode but we cannot read the file in append mode and write mode

