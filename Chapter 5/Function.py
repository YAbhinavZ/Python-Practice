
# Find Greatest of Three
def findGreatest(num1,num2,num3):
 if(num1>num2 and num1>num3):
   print(num1)
 elif(num2>num1 and num2>num3):
   print(num2)
 elif(num3>num1 and num3>num2):
   print(num3)




# Conversion of Temperature
def convert(Celcius):
  F = (9/5)*Celcius + 32
  return F

# recursive sum of N natural no.

def sumN(n):
  if(n==1): return 1

  return n + sumN(n-1)

# print(sumN(5))

# Star Pattern 1
def starPattern(n):
  i = 0
  j = 0;
  for i in range(1,n+1):
        for j in range(0,i):
            print("*" ,end=" ")
        print("")

  
# Star Pattern 2 
def starPattern2(n):
   i = 0
   j = 0
   for i in range(1,n+1):
      for j in range(2*i-1):
         print("*" , end=" ")   
      print(" ")
    

# starPattern2(3)

def printReverse(n):
    for i in range(10,0,-1):
      print(f"{n} x {i} = {n*i}")

printReverse(5)