name=input("Enter your name: ")
age_input=input("Enter your born age: ")
year=2022

age=int(year)-int(age_input)
print("Hello, ",name)
print(f" you are {age} years old ")

if(age>=5):
    print(f"{name} is going to elementary school")
elif(age>=10):
    print(f" {name} is going to middle school")
elif(age>=19):
    print(f"{name} is going to high school")
