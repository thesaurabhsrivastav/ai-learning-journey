from Dog import Dog
from Cat import Cat

class Polymorphism:

    def run(self):

        animals = [Dog(), Cat()]

        for animal in animals:
            animal.sound()


obj = Polymorphism()
obj.run()