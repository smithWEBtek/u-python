class Dog():

    species = 'mammal'

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self, number, age:
        print("WOOF!!! my name is: {n} \n ... and I am {age} years old.".format(
            n=self.name) * number, self.age)


dog1 = Dog('Sparky', 'Shepherd', 3)

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
