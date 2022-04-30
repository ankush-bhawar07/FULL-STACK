# set 
# creating an empty set using set constructor
set1 = set()
print(type(set1))

set2 = {1,2,3}
print(set2)

# Creating an set of mixed data like integers, float, strings etc.
set3 = {1,2,3,"Code", "CodeCompete", 1,1,1, "Ankush"}
print(set3)

# set methods

# add() methods
set3.add("Python")
print(set3)

# update() method
set3.update(["C", "Java"])
print(set3)

# remove() method
set3.remove("Code")
print(set3)

# discard() method
set3.discard("Ankush")
print(set3)

# pop() method
set3.pop()
print(set3)

new_set1 = {1,2,3}
new_set2 = {2,3,4}

print(new_set1.union(new_set2))
print(new_set1 | new_set2)

print(new_set1.intersection(new_set2))
print(new_set1 & new_set2)