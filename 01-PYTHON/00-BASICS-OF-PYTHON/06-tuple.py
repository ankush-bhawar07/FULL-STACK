# tuple
# creating a tuple using tuple constructor
tuple1 = tuple()
print(type(tuple1))

# creating a tuple using parentheses ()
tuple2 = ()
print(type(tuple2))

# creating tuple with values ( numbers )
data1 = (1,2,3)
print(type(data1))
print(data1)
print(data1[-1])

# creating tuple with values ( mixed values like numbers, string, another tuple ) )
data2 = (1,2,3,4,4,4,4, 1.1, "CodeCompete", data1)
print(data2)

# printing length of tuple
print(len(data2))

# accessing elements from tuple using index numbers
print(data2[-1])
print(data2[-1][-1])

# tuple slicing ( accessing group of elements )
print(data2[3:])
print(data2[-3:])

# methods
t1 = (1,2,3)
t2 = (4,5,6,2,2,2,2,2,2,2,7)

# concatinatin tuples
t3 = t1 + t2

# methods
# count()
print(t3.count(2))

# index()
print(t3.index(7))

# we can aslo create tuple without parentheses (), but it's not recommended 
newTuple = 1,2,3,4
print(type(newTuple))
print(newTuple)

# tuple is imutable but it can be reassigned
newTuple = ("hello","hi")
print(newTuple)

# can't delete items but we can delete an entire tuple
del newTuple