str = input("Enter Your Sentence : ")
x = int(input("Enter number of charectors you want : "))

if x > len(str):
    print("You have entered invalid number")
elif x == len(str):
    print(str[0:x])
elif str[0:x+1] == " ":
    print(str[0:x])
else:
    for i in range(x,0,-1):
        if str[i] == " ":
            print(str[0:i])
            break