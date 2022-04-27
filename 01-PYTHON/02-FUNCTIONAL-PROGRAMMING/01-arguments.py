def update(x):
    x = 7
    print("id of x :", id(x), "value : ", x)

a = 5
print("id of a :", id(a), "value : ", a)
update(a)
print("id of a :", id(a), "value : ", a)

def update_list(lst2):
    lst2[0] = 10
    print("id of lst2 :", id(lst2), "value : ", lst2)

lst1 = [15,20,30]
print("id of lst1 :", id(lst1), "value : ", lst1)
update_list(lst1)
print("id of lst1 :", id(lst1), "value : ", lst1)
