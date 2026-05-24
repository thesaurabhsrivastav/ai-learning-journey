class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Rahul", 88)
s2 = Student("Ananya", 95)

s1.display()
s2.display()