# Creating an empty dictionary
d1 = dict()
print(type(d1))

d2 = {}
print(type(d2))

d3 = {"Ankush": 8830400295, "CodeCompete": "08830400295", 3: "Three"}
print(d3)

print(d3["Ankush"])
print(d3.keys())
print(d3.values())

# accessing using key
print(d3["Ankush"])

# get() ( accessing using get method )
print(d3.get("Ankushsd", "Not found"))

# add()
d3["John"] = 348763287234832487
print(d3)

# update()
oldDict = {
"sjkdhksj": "sdmnbsm",
"jsdhgfdsjf": "dnbvsvdsbdvsb"
}
d3.update(oldDict)
print(d3)

# pop() ( return deleted value back)
print(d3.pop("Ankush"))

# merge
a1 = ["a", "b", "c"]
a2 = [1,2,3]     
a3 = dict(zip(a1,a2))
print(a3)

# clear()
d3.clear()
print(d3)

# del function

# deleting item
del d3[3]
print(d3)

# deleting whole dictionary
del d3
# print(d3) ( it will through error, because we don't have d3 now )