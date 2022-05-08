# Filter dictionary to contain keys present in the given list

d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}
l1 = ['A', 'C', 'F']

# solution 1
d2 = {}

for i in l1:
    d2[i] = d1[i]
print(d2)

# solution 1
d3 = {key: d1[key] for key in l1}
print(d3)
