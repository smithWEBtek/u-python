# def lesser_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         print(min([a, b]))
#         return min([a, b])
#     elif a % 2 != 0 and b % 2 != 0:
#         print(max([a, b]))
#         return max([a, b])


# lesser_of_two_evens(2, 4)
# lesser_of_two_evens(2, 5)
# lesser_of_two_evens(6, 8)
# lesser_of_two_evens(8, 2)

# --------------------------------------


# def animal_crackers(text):
#     a = text.split()[0]
#     b = text.split()[1]

#     print(a[0] == b[0])
#     return a[0] == b[0]


# animal_crackers('Levelheaded Llama')
# animal_crackers('Crazy Kangaroo')


# def old_macdonald(name):
#     arr = list(name)
#     arr[0] = name[0].upper()
#     arr[3] = name[3].upper()
#     result = ''.join(arr)
#     print(result)
#     return result


# old_macdonald('macdonald')

# def master_yoda(text):
#     arr = text.split()
#     new_arr = []
#     i = len(arr) - 1
#     while i >= 0:
#         new_arr.append(arr[i])
#         i -= 1
#     print(' '.join(new_arr))
#     return (' '.join(new_arr))


# master_yoda('I am home')


# def paper_doll(string):
#     new_string = ''
#     i = 0
#     for l in string:
#         new_string = new_string + (string[i] * 3)
#         i += 1
#     print(new_string)
#     return new_string


# paper_doll('Hello')
# paper_doll('Goodbye')

# ----------------------------------------------------------------------------
# BLACKJACK: Given three integers between 1 and 11,
#
# if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. # # Finally, if the sum (even after adjustment) exceeds 21, return 'BUST


# def blackjack(a,b,c):
#     nums = list(a,b,c)
#     if (sum(nums) > 21) and (11 in (nums)):
#         return sum(nums) - 10
#     elif sum(nums) <= 21:
#         return sum(nums)
#     elif sum(nums) > 21:
#         return 'BUST'


# def summer_69(arr):
#     total = 0
#     add = True

#     for n in arr:
#         while add:
#             if n != 6:
#                 total += n
#                 break
#             else:
#                 add = False
#         while not add:
#             if n != 9:
#                 break
#             else:
#                 add = True
#                 break
#     print(total)
#     return total


# summer_69([1, 3, 5])
# summer_69([4, 5, 6, 7, 8, 9])
# summer_69([2, 1, 6, 9, 11])


# def spy_game(arr):
#     code = [0, 0, 7]
#     test = []
#     for n in arr:
#         if n == 0:
#             test.append(n)
#         elif n == 7:
#             test.append(n)
#             break
#     if test == code:
#         print('true')
#         return True
#     else:
#         print('false')
#         return False


# spy_game([1, 2, 4, 0, 0, 7, 5])
# spy_game([1, 0, 2, 4, 0, 5, 7])
# spy_game([1, 7, 2, 0, 4, 5, 0])

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


def square(n):
    a = []
    if n % 2 == 0:
        a.append(n*n)
    b = set(a)
    return list(b)


a = list(range(1, 33))
print(list(map(square, a)))
