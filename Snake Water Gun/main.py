import random
computer = random.choice([-1,0,1])
user = input("Enter your choice :")
dict = {
   "s" : -1,
   "g" : 0,
   "w" : 1
}
reverseDic = {
    1 : "Water",
    0 : "Gun",
    -1: "Snake"
}

userNum = dict[user]

print("Your Choice : ", reverseDic[userNum])
print("Computer Choice : ",reverseDic[computer])

if(userNum==computer):
    print("Its a draw")
else :
    if(userNum==-1 and computer==1):
        print("You Win!")
    elif(userNum==-1 and computer== 0):
        print("Computer Wins")
    elif(userNum==0 and computer==1):
        print("Computer Wins")
    elif(userNum==0 and computer==-1):
        print("You Win!")
    elif(userNum==1 and computer==0):
        print("You Win!")
    elif(userNum==1 and computer==-1):
        print("Computer Wins!")
    else:
        print("Something went wrong")
