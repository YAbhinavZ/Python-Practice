class Employee:
    language = "py" # This is a class attribute
    salary   = 1200000
    def getInfo(self):
        print(f"The language is {self.language}")
    @staticmethod
    def greet():
        print("Hi Good Morning")

abhinav = Employee()
abhinav.name = "Abhinav" # This is an instance attribute
abhinav.age = 21
abhinav.greet()
