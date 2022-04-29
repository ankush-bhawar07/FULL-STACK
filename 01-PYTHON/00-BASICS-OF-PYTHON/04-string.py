name = "CodeCopmpete"

# print whole string
print(name)

# print first character
print(name[0])

# print second character
print(name[1])

# print last character
print(name[-1])

# string slicing
print(name[0:4])
print(name[:4])

print(name[4:-1])
print(name[4:])

# string methods

# capitalize()
name_capitalized = name.capitalize()
print(name_capitalized)

# upper()
name_upper = name.upper()
print(name_upper)

# swapcase() 
name_swapcase = name.swapcase()
print(name_swapcase)

# count()
print(name.count("C"))
print(name.count("Code"))

# replace()
name_new = name.replace("C", "c")
print(name_new)

# find()
print(name.find("p"))

# isalpha()
print(name.isalpha())

# isdigit()
print(name.isdigit())

# islower()
print(name.islower())

# isupper()
print(name.isupper())

# len() function
print(len(name))

# string concatination
str1= "Code"
str2 = "Compete"
str3 = str1 + str2
print(str3)
