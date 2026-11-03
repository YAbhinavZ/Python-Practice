# import random;
# # 1 check whether the file contains "Twinkle"
# # with open("poems.txt") as f:
# #     fileContent = f.read()
# #     if(fileContent.find("Twinkle")==-1):
# #         print("Not exists")
# #     else :
# #         print("Does exits")

# #  2 Game() Score
# def game():

#  score = 0
#  userNum = 0
#  computerNum = 0
 
#  while(userNum!=-1):
#   userNum = int(input("Guess the number between 1 to 10 : "))
#   guessNum = random.randint(1,10)
#   computerNum = random.randint(1,10)
#   if(abs(guessNum-computerNum)>abs(guessNum-userNum)):
#     score = score+1
#     print("You win")

#   elif(abs(guessNum-computerNum)>abs(guessNum-userNum)): 
#     print("Tie")

#   else:
#     if(score>0):
#      score = score-1
#     print("You lose")

#  print("Game ends, Your Score : ",score)

# # Checking the Hi_Score 
#  with open("Hi_Score.txt", "r") as gameFile:
#     gameContent = gameFile.read()
#     if gameContent == "":
#      print("File is empty")
#     else:
#      highestScore = int(gameContent)

#      if score > highestScore:
#         print("You beat the highest score")

#  with open("Hi_Score.txt", "w") as gameFile:
#             gameFile.write(str(score))

 
# 3 Find out the table of 2 to 20 

# def generateTable(n):
#    table = ""
#    for i in range(1,11):
#       table += f"{n} X {i} = {n*i} \n"
 
#    with open(f"table/table_{n}","w") as f:
#       f.write(table)


# for i in range(2,21):
#    generateTable(i)


with open("Donkey.txt") as Donk:
   fileContent = Donk.read()
   newFile =  fileContent.replace("Donkey","#####")
   with open("Donkey.txt",'w') as DW :
       DW.write(newFile)
   
   
  
 


