num1=input("Enter your first number: ")
num2=input("Enter your second number")
num3=input("Enter your third number: ")

user_input=input("do you want to find max or min: ")

#find the max number
if(user_input=="max"):
    if(num1>=num2 and num1>=num3):
        print("Max number is: ",num1)
    elif(num2>=num1 and num2>=num3):
        print("max number is: ",num2)
    else:
        print("max number is: ",num3)
        
# calculate the min number
if(user_input=="min"):
    if(num1<=num2 and num1<=num3):
        print("min number is :",num1)
    elif(num2<=num1 and num2<=num3):
        print("min numbr is :",num2)
    else:
        print("min number is: ",num3)
        
