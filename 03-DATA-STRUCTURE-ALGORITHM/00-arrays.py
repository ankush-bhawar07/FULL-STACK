import array
# import array as arr
# from array import *

a = array.array('d', [2.5, 4.9, 6.7])

print(a)
print(type(a))

for i in range(len(a)):
    print(a[i])
    i = i + 1