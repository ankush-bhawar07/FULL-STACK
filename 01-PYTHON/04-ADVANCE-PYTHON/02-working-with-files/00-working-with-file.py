f = open('00-myFile','r')

# print(f.read())
# print(f.readline(), end="")
# print(f.readline(), end="")
# print(f.readline(), end="")
# print(f.readline(), end="")


# f1 = open('00-myFile2', 'w')
# f1.write("Hey, this is new file\n")

f1 = open("00-myFile2", 'a')
f1.write("Hey, This is new line\n")

# for data in f:
#     print(data)

f2 = open("00-myFile3", "w")

for data in f:
    f2.write(data)