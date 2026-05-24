class Animal:

    def eats(self):
        print("Animal eats food")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


d = Dog()

d.eats()
d.bark()