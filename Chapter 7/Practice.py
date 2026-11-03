class Programmer :
    company  = "Microsoft"
    def __init__(self,name , salary,role):
        self.name = name
        self.salary = salary
        self.role = role

Emp1 = Programmer("Abhinav",230000,"SDE")
Emp2 = Programmer("Yash",530000,"Dev")
Emp3 = Programmer("Imran",130000,"SDE")
Emp4 = Programmer("Hifsa",630000,"Dev")

import math
class Calculator:
    def __init__(self,n):
        self.n = n
    @staticmethod
    def greet():
        print("Hello guys!")
    def square(self):
        return self.n*self.n
    def cube(self):
        return self.n*self.n*self.n
    def root(self):
        return math.sqrt(self.n)


# class demo:
#     a

# obj = demo()
# obj.a = 0

class Train:
    seats = 0
    def bookTicket():
        print("Ticket is booked")
    
    def getStatus(self):
        return self.seats
    
    def fair():
        print("Detail list of fair")

train1 = Train()
train1.seats = 24
print(train1.seats)