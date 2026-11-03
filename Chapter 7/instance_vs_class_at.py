class Employee:
    language = "py" # This is a class attribute
    salary   = 1200000

abhinav = Employee()
abhinav.name = "Abhinav" # This is an instance attribute
abhinav.age = 21
print(abhinav.name, abhinav.salary, abhinav.age)
