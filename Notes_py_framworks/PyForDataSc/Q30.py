# Q30. 30. Create a class Student with methods to calculate and display grade.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def grade(self):
        return 'A' if self.marks >= 90 else 'B' if self.marks >= 75 else 'C'
s = Student('John', 92)
print(s.grade())