items=["vadai","soda","sanwich"]
calculate=0
cost=[30,20,100]

#using print the manu card
print("Menu:")
for i in range(0,len(items)):  
 print(items[i])
 
#calculate the total cost
for index in range(0,len(items)):
    buy=input("how many "+ items[index] +" do you want: ")
    calculate+=int(buy)+cost[index]

print("total cost",calculate)

print("please pay the bill")
amount=input("enter your amount")
change_amount=int(amount)-calculate
print("your change amount ",change_amount)