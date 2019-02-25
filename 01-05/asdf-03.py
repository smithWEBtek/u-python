import re
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

even_letters = []
# for letter in letters[::2]:
#     even_letters.append(letter)

# for letter in "catfight":
#     even_letters.append(letter)

# shortlist = letters[::6]
# print(shortlist)

# even_letters = list(letters[::2])
# print(even_letters)

# list2 = [letter for letter in letters[::6]]
# print(list2)

# list3 = []
# for l in letters:
#     list3.append(l)
# print(list3)


# # myrange = x for x in range(0, 5)
# print([x for x in range(0, 5)])

# print([l.upper() for l in letters if l > 'm'])


# cel = [0, 10, 20, 34.5]
# fah = [((9/5) * t + 32) for t in cel]
# print(fah)

# st = 'Print only the words that start with s in this sentence'
# for word in st.split():
#     # if word[0].lower() == 's':
#     if re.match("s", word):
#         print(word)


# mylist = []
# for n in range(1, 50):
#     if n % 3 == 0:
#         mylist.append(n)
# print(mylist)

print([n for n in range(1, 50) if n % 3 == 0])
