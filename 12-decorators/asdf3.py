def new_decorator(original_func):

    def wrap_func():

        print('***********************************************')
        print('Some extra code, BEFORE the original function')
        print('***********************************************')

        print('\n \t ', original_func(), '\n')
        # print(original_func())

        print('***********************************************')
        print('Some extra code, AFTER the original function')
        print('***********************************************')

    # return wrap_func() # calls it immediately upon execution of code, can't assign to variable this way
    return wrap_func


def hello():
    return ('Hi there.')


# def func_needs_decorator():
#     # print('I want to be decorated!!')
#     return 'I want to be decorated!!'


# print(new_decorator(hello))
# new_decorator(hello)

# decorated_func = new_decorator(func_needs_decorator)
# decorated_func()

@new_decorator
def func_needs_decorator():
    # print('I want to be decorated!!')
    return 'I want to be decorated!!'


# @new_decorator wraps this function, because it is setup to receive it as an argument
func_needs_decorator()

# print(func_needs_decorator())
