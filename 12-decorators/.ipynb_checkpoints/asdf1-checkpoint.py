# ________________________________________________________________________


def hello(name='Jose'):
    print(f'The hello function has been executed, with name: {name}')

    def greet():
        print('\t This is the greet() func inside hello!')
        return '\t This is the greet() func inside hello!'

    def welcome():
        print('\t This is the welcome() func inside hello!')
        return '\t This is welcome() inside hello'

    print('I am going to return a function')
    if name == 'Jose':
        return greet
    else:
        return welcome


myvar = hello
# myvar = hello('Jose')
# myvar = hello('Bob')

myvar
