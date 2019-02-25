
from functools import reduce
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
# def square(n):
#     return n * n


# print(list(map(square, nums)))


# def rev(string):
#     # print(string[::-1])
#     return string[::-1]


# print(rev(letters))
# rev(letters)

# def splicer(string):
#     if len(string) % 2 == 0:
#         return string
#     else:
#         return


# def even_capper(string):
#     if len(string) % 2 == 0:
#         return string.upper()

# print(list(filter(splicer, pets)))


# print(' '.join(list(map(even_capper, list(filter(even_capper, pets))))))
# print(list(lambda p: even_capper(pets)))


# def even(n):
#     return n % 2 == 0


# def square(n):
#     return n ** 2


nums2 = list(range(1, 222))
# nums2even = list(filter(even, nums2))
# nums2even_squared = list(map(square, nums2even))
# print(nums2even_squared)

# c = list(filter(lambda n: n % 2 == 0, nums2))
# # print("evens: ", c)

# d = list(map(lambda n: n**2, c))
# print("squares: ", d)


def rev(word): return word[::-1]


print(list(map(rev, pets)))
# print(list(map(lambda n: n[::-1], pets)))
