


















def add_function(num1,num2):
    return num1+num2

def subtract_function(num1,num2):
    return num1-num2

def multiply_fuction(num1,num2):
    return num1*num2

def divide_function(num1,num2):
    return num1/num2

choice = int(input("Enter your Chpoice[1-Add,2-Subs,3-multiply,4-divide}"))

num1 = int(input("Enter First number"))
num2 = int(input("Enter Second number"))

if(choice==1):
    add = add_function(num1,num2)
    print(add)

elif(choice==2):
    subs=subtract_function(num1,num2)

elif(choice==3):
    mult=multiply_fuction(num1,num2)

elif(choice==4):
    divide=divide_function(num1,num2)

else:
    print("You Didn't Select Anything")