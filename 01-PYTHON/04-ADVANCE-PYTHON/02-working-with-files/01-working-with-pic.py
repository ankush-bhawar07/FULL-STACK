f = open("01-pic.png", "rb")

# for i in f:
#     print(i)

f1 = open("01-pic2.JPG", "wb")
for i in f:
    f1.write(i)