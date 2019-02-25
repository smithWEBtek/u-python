# GUESSING GAME
from random import randint

solution = randint(1, 100)
data = {
    'solution': solution,
    'current_guess': 0,
    'last_guess': 0,
    'diff': 0,
    'count': 0
}

print("The solution is: ", data['solution'])
print('----------------------------------------')
print('choose a number between 1 and 100')
print('if you choose correctly, you will get a WIN message')
print('if you choose incorrectly, you will get a WARMER or COLDER message')

user_input = input("please guess a number from through 1 and 100:    ")
data['last_guess'] = int(user_input)
data['diff'] = abs(int(data['solution']) - int(user_input))
print(data)

while data['diff'] != 0:
    user_input = input("please guess a number from through 1 and 100:    ")
    data['current_guess'] = int(user_input)
    data['diff'] = abs(int(data['solution']) - int(user_input))

    if data['current_guess'] > 100 or data['current_guess'] < 1:
        print('OUT OF BOUNDS')
        continue

    while data['solution'] != data['current_guess']:
        if data['diff'] >= abs(data['solution'] - data['current_guess']) and data['diff'] < 10:
            data['diff'] = abs(data['solution'] - data['current_guess'])
            print("WARM!")

        elif data['diff'] <= abs(data['solution'] - data['current_guess']) and data['diff' > 10]:
            data['diff'] = abs(data['solution'] - data['current_guess'])
            print("COLD!")

        if data['diff'] > abs(data['solution'] - data['current_guess']):
            data['diff'] = abs(dat
                               a['solution'] - data['current_guess'])
            print("WARMER!")
        elif data['diff'] < abs(data['solution'] - data['current_guess']):
            data['diff'] = abs(data['solution'] - data['current_guess'])
            print("COLDER!")

        elif data['current_guess'] == data['solution']:
            print('YOU GUESSED {s}} RIGHT! It only took you {c} attempts!'.format(
                c=data['count'], s=data['solution']))
