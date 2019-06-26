class Student:
    def __init__(self, name, major, grade, gpa):
        self.name = name
        self.major = major
        self.grade = grade
        self.gpa = gpa

    def is_honour(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
