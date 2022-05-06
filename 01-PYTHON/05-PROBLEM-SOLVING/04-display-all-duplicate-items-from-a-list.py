import collections

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

# solution 1
# duplicates = []
# for item, count in collections.Counter(sample_list).items():
#     if count > 1:
#         duplicates.append(item)

# print(duplicates)

# solution 2
exist = {}
duplicates = []

for item in sample_list:
    if item not in exist:
        exist[item] = 1
    else:
        duplicates.append(item)
print(duplicates)
