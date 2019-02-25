def cool(func=0):
    def not_cool(name):
        return f'{name}, that is NOT cool.'
    def medium_cool(name):
        return  f'{name}, I am kind of cool.'
    def super_cool(name):
        return  f'{name}, I am very cool!'
    
    if func == 1:
        return not_cool
    elif func == 2:
        return medium_cool
    elif func == 3:
        return super_cool
    else:
        return 'Nobody knows how cool I am.'
    
    
        

var1 = cool(1)
var2 = cool(2)
var3 = cool(3)

var1('Francis')
var2('Beork')
var3('Freda')