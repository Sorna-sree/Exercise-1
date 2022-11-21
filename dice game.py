import random

user_1=True
user_2=False
user_1_point=0
user_2_point=0
streak_1=0
streak_2=0
max_1=0
max_2=0

#it is used to generate the random number
def random_num():
    random_num=random.randint(0,12)
    return random_num


#gets another chance to roll 
def chance():
    if(random_number==1 or random_number==4 or random_number==6 or random_number==12):
       return 1
    else:
       return 0 
   
#using gets 5 additional points       
def additional_points():
    if(streak_1==3 or streak_2==3):
        return 5

#using to subract the one point
def subract():
   if(random_number==0):
       return 1 
   
#roll 9 miss the turn
def miss_turn():
    if(random_number==9):
        return False
    
#play maximum of 50 times   
def  max_time():
    if(max_1==50 or max_2==50):
        return False  
    
if(user_1):
    max_1+=1
    user_1=False
    user_2=True
    random_number=random_num()
    user1_chance=chance(random_number)
    if(user1_chance==1):
        user_1_point+=1
        user_1=True
        user_2=False
        streak_1+=1
        additional_points(streak_1)
        user_1_point+=5
user_1_point-=subract(random_number)
user1=miss_turn(max_1)


if(user_2):
    max_2+=1
    user_2=False
    user_1=True
    random_number=random_num()
    user2_chance=chance(random_number)
    if(user2_chance==1):
        user_2_point+=1
        user_2=True
        user_1=False
        streak_2+=1
        additional_points(streak_2)
        user_2_point+=5
user_2_point-=subract(random_number)
user2=miss_turn(random_number)
user_2=max_time(max_2)

if(user_1_point>user_2_point):
    print("user 1 is win",user_1_point)
else:
    print("user 2 is win",user_2_point)
