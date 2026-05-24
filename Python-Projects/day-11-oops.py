class Student:
    school = "ABC School"   # class variable

    def __init__(self, name):
        self.name = name    # instance variable

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name

Student.change_school("XYZ School")

print(Student.school)