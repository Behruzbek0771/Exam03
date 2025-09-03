class Student:
    def __init__(self, name, year, course):
        self.name = name
        self.year = year
        self.course = course
    
    def introduce(self):
        return f"My name is {self.name}, I am {self.year} years old, studying in {self.course}nd course."

s = Student("Ali", 20, 2)
print(s.introduce())