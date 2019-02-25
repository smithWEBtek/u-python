def cool(func=0):
    def not_cool(name='blank'):
        if name != 'blank':
            return f'{name}, that is NOT cool.'
        else:
            return "You might be cool, but you have no name."

    def medium_cool(name='blank'):
        if name != 'blank':
            return f'{name}, I am kind of cool.'
        else:
            return "You might be cool, but you have no name."

    def super_cool(name='blank'):
        if name != 'blank':
            return f'{name}, I am very cool!'
        else:
            return "You might be cool, but you have no name."
    if func == 1:
        return not_cool
    elif func == 2:
        return medium_cool
    elif func == 3:
        return super_cool
    else:
        return 'Nobody knows how cool I am.'


# creates a version of the cool function, with a custom argument
var1 = cool(1)
var2 = cool(2)
var3 = cool(3)

# since the cool function returns a function, you can pass an arg to the inner function
print(var1('Francis'))  # Francis, that is NOT cool.
print(var2('Beork'))  # Beork, I am kind of cool.
print(var3('Freda'))  # Freda, I am very cool!

# calling the 3 variables, without a name argument
print(var1())  # You might be cool, but you have no name.
print(var2())  # You might be cool, but you have no name.
print(var3())  # You might be cool, but you have no name.
