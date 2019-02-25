
# def hello():
#     print('hello')
#     return 'hello'


# hello()

# greet = hello
# # greet()

# del hello

# greet()

# ________________________________________________________________________

def hello(name='Jose'):
    print(f'The hello function has been executed, with name: {name}')

    def greet():
        #print('\t This is the greet() func inside hello!')
        return '\t This is the greet() func inside hello!'

    def welcome():
        return '\t This is welcome() inside hello'

    print(greet())
    print(welcome())
    print('End of the hello function')


hello()
