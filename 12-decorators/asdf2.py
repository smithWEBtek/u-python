# PASSING A FUNCTION AS AN ARGUMENT


def hello():
    return 'Hi Jose!'


def other(some_func):
    print('Other code runs here first ...')
    print("The output of only printing the some_func argument: \n", some_func)
    print("The output of calling () on the some_func argument: \n", some_func())


other(hello)
