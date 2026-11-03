class Employee:
    language = "py" # This is a class attribute
    salary   = 1200000

    def __init__(self,name,salary,language):
       self.name = name
       self.salary = salary
       self.language = language



Student1 = Employee("Rohan",120000,"PYTHON")

print(Student1.name,Student1.salary)
