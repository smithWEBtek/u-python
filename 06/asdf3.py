import math
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


# def myfunc(a, b):
#     return sum((a, b))*.05


# print(myfunc(40, 60))

# def myfunc(**asdf):
#     if 'fruit' in asdf:
#         # review String Formatting and f-strings if this syntax is unfamiliar
#         print(f"My favorite fruit is {asdf['fruit']}")
#         # review String Formatting and f-strings if this syntax is unfamiliar
#         print(f"My favorite song is {asdf['song']}")
#     else:
#         print("I don't like fruit")


# myfunc(fruit='pineapple', song='Rainbow')


# def myfunc(*args, **kwargs):
#     if 'fruit' and 'juice' in kwargs:
#         print(
#             f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
#         print(f"May I have some {kwargs['juice']} juice?")
#     else:
#         pass

# myfunc('eggs', 'spam', fruit='cherries', juice='orange')


# def vol(rad):
#     return (4/3 * 3.14) * rad ** 3


# print(vol(2))


# def ran_check(num, low, high):
#     if num in range(low, high):
#         print('{n} is in the range between {l} and {h}'.format(
#             n=num, l=low, h=high))


# ran_check(5, 2, 7)


# def ran_bool(num, low, high):
#     return num in range(low, high)


# print(ran_bool(2, 5, 7))
# print(ran_bool(6, 5, 7))


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33

# def myfunc(phrase):
#     uppers = []
#     lowers = []

#     for l in phrase:
#         if l == l.upper():
#             uppers.append(l)
#         elif l == l.lower():
#             lowers.append(l)
#     print("uppers: ", len(uppers))
#     print("lowers: ", len(lowers))


# myfunc('BradleySmith')
# myfunc('WeAreFamily')

# def myfunc(phrase):
#     data = {'uppers': 0, 'lowers': 0}
#     for l in phrase:
#         if l.isupper():
#             data['uppers'] += 1
#         elif l.islower():
#             data['lowers'] += 1
#     print('Original String : ', phrase)
#     print("No. of Upper case characters : ", data['uppers'])
#     print("No. of Lower case Characters : ", data['lowers'])
#     print('-----------------------------------------------------')


# myfunc('BradleySmith')
# myfunc('WeAreFamily')

# s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
# myfunc(s)

# --------------------------------------------------------------

# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

# def uniker(l):
#     # unlist = set(l)
#     # relist = list(unlist)
#     # print(relist)

#     print(list(set(l)))
#     return list(set(l))


# uniker([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])
# --------------------------------------------------------------

# def multi(lst):
#     res = 1
#     for n in lst:
#         res *= n
#     print(res)
#     return res


# multi([1, 2, 3, -4])
# multi([2, 2, 2])
# --------------------------------------------------------------
# palindrome_checker

# def pal(word):
#     a = list(word)
#     a.reverse()
#     a = ''.join(a)
#     print(a)
#     return a == word


# print(pal('madam'))
# print(pal('frank'))
# print(pal('level'))

# pal('madam')
# pal('frank')
# pal('level')
# --------------------------------------------------------------
# pangram checker

# def pan(phrase):
#     alf = "abcdefghijklmnopqrstuvwxyz"

#     a = phrase.split(' ')
#     b = ''.join(a)
#     c = list(map(lambda l: l.lower(), b))
#     d = set(c)
#     e = list(d)
#     e.sort()
#     f = ''.join(e)
#     print(f)

#     print(alf)
#     return alf == f


# str1 = "The quick brown fox jumps over the lazy dog"
# print(pan(str1))
# --------------------------------------------------------------
# def myfunc(*args):
#     return_list = []
#     for arg in args:
#         if arg % 2 == 0:
#             return_list.append(arg)
#     return return_list

# --------------------------------------------------------------
# def myfunc(string):
#     array = list(string)
#     for l in array:
#         if l.lower() == l:
#             array[array.index(l)] = l.upper()
#         else:
#             array[array.index(l)] = l.lower()
#     print(''.join(array))
#     return(''.join(array))

# myfunc('aSdF')
# myfunc('ZxCV')
# myfunc('ThereAreNoWordsToDescribeHOWgoodITfeels')

# ----------------------------------------------------------------
def myfunc(string):
    array = list(string)
    i = 0
    while i < len(array):
        l = array[i]
        if i % 2 != 0:
            array[i] = l.lower()
            i += 1
        else:
            array[i] = l.upper()
            i += 1
    return(''.join(array))


myfunc('asdf')
myfunc('zxcv')
myfunc('qwer')
myfunc('therarenowordstodescribehowgooditfeels')
myfunc('aaaaaa')
# --------------------------------------------------------------
