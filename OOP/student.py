# class Student:
#     school = "AkiraChix"
#     age = 20
#     name = "Amanda"
#     code = 39

class Student:
    # all the object created from this class will have the same school name by default
    school = "AkiraChix"
    # initializing class by self and passing the attributes of the object as a parameter
    def __init__(self,first_name, last_name, age, code):
        self.first_name = first_name
        self.last_name = last_name
        self.age=age
        self.code = code

    def greet_student(self):
        # A method within a class for greeting (first parmeter: self)
        greeting = f"Hello {self.first_name}, welcome to {self.school} your code is {self.code}"
        return greeting
    
    def year_of_birth(self):
        return f"{self.first_name} was born in {2024 - self.age}"
    
    def student_fullname(self):
        return f"My name {self.first_name} {self.last_name}"
    
    def student_initials(self):
        return f"Student details: {self.first_name} {self.last_name} {self.age} {self.code}"
    
    # def student_enrollment(self):
        
