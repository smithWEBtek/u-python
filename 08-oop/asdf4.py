class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        # def about(self):
        return f"{self.title} by {self.author}, {self.pages} pages."

        # return "{t} by {a}: {p} pages.".format(t=self.title, a=self.author, p=self.pages)

    def __len__(self):
        return int(self.pages)

    def __del__(self):
        print('A Book object has been deleted.')


b1 = Book(title='My New Bike', author='Brad Smith', pages=144)
b2 = Book(title='The Dinner', author='Ann McDonald', pages=588)

print(b1)
print(len(b1))
del b1
print(b2)
