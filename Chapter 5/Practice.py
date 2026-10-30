
# Write a program to find the greatest of four numbers entered by the user.
# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# num3 = int(input("Enter Third Number: "))
# num4 = int(input("Enter Fourth Number: "))

# if(num1> num2 and num1>num3 and num1>num4):
#     print(num1,"is the greatest element")
# elif(num2> num1 and num2>num3 and num2>num4):
#     print(num2,"is the greatest element")
# elif(num3> num2 and num3>num1 and num3>num4):
#     print(num3,"is the greatest element")
# else:
#     print(num4,"is the greatest element")



# 2
Sub1 = int(input("Enter sub1 marks : "))
Sub2 = int(input("Enter sub2 marks : "))
Sub3 = int(input("Enter sub3 marks : "))

totalPercentage = ((Sub1+Sub2+Sub3)/300 )* 100


if(totalPercentage>40):
      if(Sub1>33 and Sub2>33 and Sub3>33):
          print("Pass")
      else:
           print("Fail")

else:
     print("Fail")
  

  