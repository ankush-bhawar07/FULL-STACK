num = int(input("Enter your number : "))
result = num % 2
if result == 0:
    print("Your number is even ")
else:
    print("Your number is odd")

num2 = int(input("Enter your number : "))
if(num2 >= 0):
    print("Your number is positive")
else:
    print("Your number is negetive :")

num3 = int(input("Enter your numbetr : "))
res = num3 % 2

if(res == 0):
    if(num3 > 10):
        print("Your number is even and greator than 10")
    else:
        print("Your number is even and less than 10")
elif(num3 > 10):
    print("Your number is odd and greator than 10")
else:
    print("Your number is odd and less than 10")