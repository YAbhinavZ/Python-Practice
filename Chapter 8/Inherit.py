# class Employee:
#     company = "ITC"
#     name = "Default Name"

#     def show(self):
#         print(f"The name of the Employee is {self.name} and company is {self.company}")

# class Coder:
#     language = "Python"
#     def printLanguage(self):
#         print(f"Out of all the languages here is your Language: {self.language}")

# class Programmer(Employee,Coder): 
#     company = "ITC Infotech"
#     def showLanguages(self):
#         print(f"The name is {self.company} and he is very goot at {self.langauge}")


# p1 = Programmer()

class Employee:
  a= 10
 


class Programmer(Employee):
  b= 20


class Manager(Programmer):
 c = 13

p = Manager()

print(p.b)