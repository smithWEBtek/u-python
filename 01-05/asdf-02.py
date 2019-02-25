# x = 0
# while x < 5:
#     # print('The current value of x is: {x}'.format(x=x))
#     # works now that I'm using python 3 in my aliased command
#     print(f'The current value of x is: {x}')
#     x = x + 1
#     print('-------------------------------------------------------')

# range
# mylist = list(range(1, 7))
# newList = list([1, 2, 3])
# for num in mylist:
#     newList.append(num * 5)
# print(newList)

# enumerate
# word = 'abcde'
# index_count = 0
# for letter in word:
#     print(word[index_count])
#     index_count += 1

# word = 'abcde'
# for letter in enumerate(word):
#     print(letter)

# using enumerate with tuple unpacking
# word = 'abcde'
# for index, letter in enumerate(word):
#     print(index)
#     print(letter)
#     print('\n')

# zip function based on shortest of list(s)
# nums = [1, 2, 3]
# letters = ['a', 'b', 'c', 'd', 'e']
# pets = ['cat', 'dog', 'bird']

# for item in zip(nums, letters, pets):
#     print(item)

# (1, 'a', 'cat')
# (2, 'b', 'dog')
# (3, 'c', 'bird')

# for n, l, p in zip(nums, letters, pets):
#     print(p)

# cat
# dog
# bird

# in operator
from random import Random
from random import randint
from random import shuffle
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

# min max
# random

shuffle(pets)
# print(pets)


# print(randint(0, 100))

# i = randint(0, len(pets)-1)
i = randint(0, len(pets))
print(pets[i])

name = input('what is your name?')
print(name.upper())

# fav_num = input('what is your favorite number?')
# print(int(fav_num))

fav_num = int(input('what is your favorite number?'))
print(fav_num)
