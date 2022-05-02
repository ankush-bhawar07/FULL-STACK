# Remove items from a list while iterating

# Description:
# In this question, You need to remove items from a list while iterating but without creating a different copy of a list.
# Remove numbers greater than 50

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

i = 0
n = len(number_list)

while i < n:
    if number_list[i] >  50:
        del number_list[i]
        n = n - 1
    else:
        i = i + 1
print(number_list)
