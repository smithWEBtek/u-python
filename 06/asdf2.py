letters = "abcdefghijklmnopqrstuvwxyz"
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pets = ['cat', 'dog', 'bird', 'snake', 'turtle', 'fish']
usersList = [{'name': 'Bob', 'age': 42, 'city': 'Boston'},
             {'name': 'Sue', 'age': 34, 'city': 'NYC'},
             {'name': 'Mary', 'age': 24, 'city': 'Springfield'},
             {'name': 'Phil', 'age': 55, 'city': 'Stamford'}
             ]
usersTuple = ({'name': 'Bob', 'age': 42, 'city': 'Boston'},
              {'name': 'Sue', 'age': 34, 'city': 'NYC'},
              {'name': 'Mary', 'age': 24, 'city': 'Springfield'},
              {'name': 'Phil', 'age': 55, 'city': 'Stamford'}
              )

# def check_even(num):
#     return num % 2 == 0

# print(list(filter(check_even, nums)))
# print(filter(check_even, nums))

# print(list(map(lambda p: p[1:], pets)))
# print(list(filter(lambda p: len(p) == 3, pets)))


# def pets_up():
#     print(list(map(lambda p: p.upper(), pets)))


# pets_up()

# def uppit(l):
#     return l.upper()

# print(list(map(uppit, letters)))

# print(list(filter(lambda n: n % 2 == 0, nums)))

# print(list(map(lambda l: l.upper(), letters)))


# x = 25
# def printer():
#     x = 50
#     return x

# print(x)
# print(printer())

# --------------------------------------------------
# x = 5


# def foo():
#     x = 10
#     print("local x:", x)


# foo()
# print("global x:", x)

# --------------------------------------------------
# name = 'This is a global name'

# def greet():
#     # Enclosing function
#     name = 'Sammy'

#     def hello():
#         print('Hello '+name)

#     hello()


# greet()

# print(name)

# --------------------------------------------------

# x = 50


# def func(x):
#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)


# func(x)
# print('x is still', x)
# --------------------------------------------------

# x = 50


# def func():
#     global x
#     print('This function is now using the global x!')
#     print('Because of global x is: ', x)
#     x = 2
#     print('Ran func(), changed global x to', x)


# print('Before calling func(), x is: ', x)
# func()
# print('Value of x (outside of func()) is: ', x)
# --------------------------------------------------
