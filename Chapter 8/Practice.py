# class TwoDVector:
#     def __init__(self,i,j):
#         self.i = i
#         self.j = j
#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j ")

# class ThreeDVector(TwoDVector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k = k
#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


# a = TwoDVector(2,3)
# b = ThreeDVector(2,3,4)

# a.show()
# b.show()

# class Employee:
#     salary = 20000
#     increment = 20
#     @property
#     def salaryAfterInc(self):
#         return ((self.salary )+ ( self.salary)* (self.increment*0.01));
    

# e = Employee()

# print(e.salaryAfterInc)

class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i
    
    def __add__(self,c2):
        return Complex(self.r+c2.r,self.i+c2.i)
    
    def __str__(self):
        return f"{self.r}r + {self.i}i"
  


c1 = Complex(2,3)
c2 = Complex(4,5)
    
print(c1+c2)
        