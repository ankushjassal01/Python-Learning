# read file from directory
# created files in directory where scripting working .check console for the
# run file/wdir. it show the path

# to read the file we need to open the file first
# to open the file we use open() function and it include the file path and mode of the file r w rw,b ,bw br
# linux and mac have different way of writing the file name but in windows we should use \ to escape the backslash
# my_file=open("c:\\USERS\\iphone\\My Python Learning\\MYFILE.txt")
# because \n or \t can cause problems if those are in file path so better to escape the \ before it tae effect in path
# my_file = open("e:\\study\\udemy tim bhuchuka\\2input and output files\\2.txt")
# for lines in my_file:
#     print(lines)
# my_file = open("e:\\study\\udemy tim bhuchuka\\2input and output files\\2.txt", 'r')

# open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
# 'r'       open for reading (default)
# 'w'       open for writing, truncating the file first
# 'x'       create a new file and open it for writing
# 'a'       open for writing, appending to the end of the file if it exists
# 'b'       binary mode
# 't'       text mode (default)
# '+'       open a disk file for updating (reading and writing)
# 'U'       universal newline mode (deprecated)

# The default mode is 'rt' (open for reading text). For binary random
# access, the mode 'w+b' opens and truncates the file to 0 bytes, while
# 'r+b' opens the file without truncation. The 'x' mode implies 'w' and
# raises an `FileExistsError` if the file already exists.

# we can directly open a file in directly where our current python file running like below
my_file=open('2a.txt', 'r')
# for line in my_file:
#     if 'jabberwock' in line.lower():
#         print(line, end='')
my_file.close()

# ******************************************************************************************************************** #

# with statement
# As we saw above we need to close the file after reading /writing above which make easy for our system to manage the
# resources.
# but with WITH we dont need to worry about it with statement auto close the file for us and it help us to write code
# more efficiently . in it we can assign file to variable and then pass that variable to below statements like we do in
# while ,for loops etc
with open('2a.txt', 'r') as a:
    for lines in a:
        print(lines, end='')

# it also help our file to close if our code run into errors or exception.by this our file can remain safe. without with
# we might not able to remove or alter the file until we resolve the error as file still not closed by the error code

# ******************************************************************************************************************** #
with open('2a.txt', 'r') as a:
    line = a.readline()  # this readline() will read only first line of the file
    for lines in line:
        print(lines, end='')

# ******************************************************************************************************************** #
with open('2a.txt', 'r') as a:
    line = a.readlines()  # this readlines() will read all the line of the file but put it into the list
    for lines in line:
        print(lines, end='')  # end must be use as each line have by default \n.without end o/p will have extra space

with open('2a.txt', 'r') as a:
    print(a.readlines())
# below is above  code output this readlines will give output in list
o = ["'Twas brillig, and the slithy toves\n", 'Did gyre and gimble in the wabe;\n', 'All mimsy were the borogoves,\n',
     'And the mome raths outgrabe.\n', '\n', '"Beware the Jabberwock, my son!\n',
     'The jaws that bite, the claws that catch!\n', 'Beware the Jubjub bird, and shun\n',
     'The frumious Bandersnatch!"\n',
     '\n', 'He took his vorpal sword in hand:\n', 'Long time the manxome foe he sought,\n',
     'So rested he by the Tumtum tree,\n', 'And stood a while in thought.\n', '\n',
     'And, as in uffish thought he stood,\n',
     'The Jabberwock, with eyes of flame,\n', 'Came whiffling through the tulgey wood,\n', 'And burbled as it came!\n',
     '\n', 'One two! One two! And through and through\n', 'The vorpal blade went snicker-snack!\n',
     'He left it dead, and with its head\n', 'He went galumphing back.\n', '\n',
     '"And hast thou slain the Jabberwock?\n',
     'Come to my arms, my beamish boy!"\n', '"Oh frabjous day! Callooh! Callay!"\n', 'He chortled in his joy.\n', '\n',
     "'Twas brillig, and the slithy toves\n", 'Did gyre and gimble in the wabe:\n', 'All mimsy were the borogoves,\n',
     'And the mome raths outgrabe.\n', '\n']

with open('2a.txt', 'r') as a:
    line = a.readlines()  # this make file as string but inside the list . it make each line as index position of the
    for i in line[::-1]:  # list and if we later use that in code then we can get output as list should behave
        print(i, end='')  # invert the file but as its list it reverse the order of the file lines

# ******************************************************************************************************************** #
with open('2a.txt', 'r') as a:
    line = a.read()  # read method will read the file as whole string and pass it as a string to further code
    for i in line[::-1]:  # invert the file but as its string then it make whole file as invert rather returns lines in
        print(i, end='')  # reverse order 'ankush' will be 'hsukna'
    print()


with open('2a.txt', 'r') as a:
    line = a.read()  # read method will read te file as whole string and pass it as a string to further code
    for i in line:
        print(i, end=' ')

with open('2a.txt', 'r') as a:
    print(a.read())  # just read the whole file and print

# ******************************************************************************************************************** #