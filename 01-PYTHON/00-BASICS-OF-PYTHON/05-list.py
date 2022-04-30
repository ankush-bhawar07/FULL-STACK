# create lsit using list constructor
from ast import arguments


lst1 = list()
print(type(lst1))

# create list using [] square brackets
lst2 = []
print(type(lst2))

# create a list of numbers
numbers = [1,2,3,4,5,6,7]
print(numbers)

# create list of programming languages
languages = ["Python", "PHP", "Java", "C", "C++", "Swift", "JavaScript"]
print(languages)

# create list of mixed data types
data = [1,2,3, "CodeCompete", 1.1, True, False, languages, ["HTML", "CSS", "Bootstrap"]]
print(data)

# print whole list ( Print all elements of list )
print(data)

# accessing individual elements from list using index number
print(data[0]) 
print(data[1])
print(data[-1])

# list sclicing
print(data[0:2])
print(data[2:5])
print(data[:7])
print(data[7:])

# mutable ( we can change or replace values in list )
print(data[0])
data[0] = "this is 1"
print(data[0])

# list methods
# we are creating new list to learn list methods

city = ["Pune", "Thane", "Mumbai", "Ahmednagar"]
print(city)

# append()
city.append("Nagpur")
print(city)

# insert()
city.insert(1, "Delhi")
print(city)

# remove()
city.remove("Thane")
print(city)

# reverse()
city.reverse()
print(city)

# count()

print(city.count("Pune"))
print(city)

# index()
print(city.index("Mumbai"))
print(city)

# pop()
print(city.pop(1))
print(city)

# remove()
city.remove("Nagpur")
print(city)

# sort()
city.sort()
print(city)

# clear()
city.clear()
print(city)