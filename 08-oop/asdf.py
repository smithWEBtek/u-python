class Dog():

    species = 'mammal'

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self, number):
        print("WOOF!!! my name is: {n} \n".format(n=self.name) * number)


# dog1 = Dog('Sparky', 'Shepherd')

# print(dog1.name)
# print(dog1.breed)
# print(dog1.species)
# print(dog1.bark(3))

class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def get_circumference(self):
        return self.radius * self.pi * 2


circ1 = Circle(4)

print(circ1.get_circumference())
