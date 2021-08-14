# Binary file
#
# processing binary data like image file and to store the variables which we can use late in program
# to write the binary file or open binary file . we can specify the mode as 'b'
# we can write the string /integers directly to binary files it need to be convert first to bytes first
# python provide the built in functions


# with open("binary.txt", 'bw') as b_file:  # with binary+write mode
#     for s in range(5):
#         b_file.write(bytes(s))  # b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' without list of int(s) it will pass the 0
#         #                       # for multiple times
# with open('binary.txt', 'br') as bfile:
#     print(bfile.read())
#
# with open("binary.txt", 'bw') as b_file:  # with binary+write mode
#     for s in range(20):
#         b_file.write(bytes([s]))
#
# with open('binary.txt', 'br') as bfile:
#     print(bfile.read())

# with open("binary.txt", 'ba') as b_file:  # with binary+append mode
#     for s in range(20):
#         b_file.write(bytes([s]))  # we are passing list of the integers in list to byte function
#
# with open('binary.txt', 'br') as bfile:
#     print(bfile.read())

a = 65534  # FF FE
b = 65535  # FF FF
c = 65536  # 00 01 00 00
x = 2998302  # 00 2D C0 1E

with open("binary2.txt", 'bw') as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))  # 2 is length and big here is big int type byteorder
    bin_file.write(b.to_bytes(2, 'big'))  # to_byte to convert the int to bytes (big or little)
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'little'))


with open('binary2.txt', 'br') as bfile:
    print(bfile.read())


with open("binary2.txt", 'rb') as bin_file:
    e = int.from_bytes(bin_file.read(2), 'big')  # to change the from_bytes confirm the data of file
    print(e)
    f = int.from_bytes(bin_file.read(2), 'big')
    print(f)
    g = int.from_bytes(bin_file.read(4), 'big')
    print(g)
    h = int.from_bytes(bin_file.read(4), 'big')
    print(h)
    i = int.from_bytes(bin_file.read(4), 'big')
    print(i)
    j = int.from_bytes(bin_file.read(4), 'little')
    print(j)
