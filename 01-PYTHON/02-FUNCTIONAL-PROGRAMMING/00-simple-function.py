def greet(name):
    print("Hello", name)

greet("Ankush")

def add(num1, num2):
    return num1 + num2

result = add(2,3)
print(result)

def cal(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    return add, sub, mul, div

add, sub, mul, div = cal(1,2)
print(add, sub, mul, div)
