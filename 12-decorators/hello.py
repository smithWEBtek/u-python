def hello():
    return 'Hi Jose!'

# accepts a function as argument


def other(func):
    print('Other code runs here ...')
    print(func())


# call, and pass in function as argument
# print(func()) will call it as a function
other(hello)
