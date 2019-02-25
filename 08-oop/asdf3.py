class Animal():

    def speak(self):
        print(self.speak)
        raise NotImplementedError("Subclass needs to call this")


class Dog(Animal):
    def __init__(self, name, breed, says):
        self.name = name
        self.breed = breed
        self.says = says

    def speak(self):
        return "My name is {n}. \n I am a {c} and I {s}".format(n=self.name, c=self.__class__.__name__, s=self.says)


class Cat(Animal):
    def __init__(self, name, breed, says):
        self.name = name
        self.breed = breed
        self.says = says

    def speak(self):
        return "My name is {n}. \n I am a {c} and I {s}".format(n=self.name, c=self.__class__.__name__, s=self.says)


dog1 = Dog(name='Fido', breed='Collie', says='Woof!')
# print(dog1.speak())

cat1 = Cat(name='Garfield', breed='Calico', says='Meow!')
# print(cat1.speak())


def pets_speak(pets):
    for pet in pets:
        print(pet.speak())


pets_speak([dog1, cat1])
