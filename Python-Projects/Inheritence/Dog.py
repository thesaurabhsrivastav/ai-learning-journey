from Animal import Animal

class Dog(Animal):

    def bark(self):
        print("Dog barks")


d = Dog()

d.eats()
d.bark()