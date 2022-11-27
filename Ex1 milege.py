#calculate the milege

petrol=input("How many litres of petrol you have: ")
km=input("how many km you have to drive")

milege=int(km)/int(petrol)
print(milege)

if(milege>=30):
    print("you have to fill the tank again")