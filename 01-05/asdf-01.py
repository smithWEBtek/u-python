# print('hello \npython')
# print('hello \tpython')
# print(len('hello'))

# import math
# letters = "abcdefghijklmnopqrstuvwxyz"
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# slice
# print(letters[2:5])
# print(letters[0:3])
# print(letters[:3])
# print(letters[3:6])
# print(letters[2:8])

# step
# print(nums[0:19:7])
# print(nums[::])
# print(nums[::5])
# print(nums[2::5])

# print(type(nums))
# print(type(letters))

# reverse
# print(nums[::-1])
# print(letters[::-1])


# mystring = 'Hello World'
# # print(mystring[-3])
# print('Hello World'[-3])
# 'Hello World'[-3]

# x = 'fish'
# if x == 'dog':
#     print('it is a dog')
# elif x == 'bird':
#     print('it is a bird')
# elif x == 'cat':
#     print('it is a cat')
# else:
#     print('X = {}'.format(x))

# print(4 * (6 + 5))
# print(4 * 6 + 5)
# print(4 + 6 * 5)


# chuck = (3 + 1.5 + 4)
# print(type(chuck))

# print(math.sqrt(9))


# s = 'hello'
# Reverse the string using slicing
# print(s[:]

# a = 0
# l = []
# l.append(a) * 3
# print(l)


# a = (1, 2, 3)
# print(a)
# print(type(a))


# list5 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
# print(set(list5))


# with open('asdf4.txt', mode='r') as f:
#     print(f.read())
#     print('--------------------------------')


letters = "abcdefghijklmnopqrstuvwxyz"
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pets = ['cat', 'dog', 'bird']
users = ({'name': 'Bob', 'age': 42, 'city': 'Boston'},
         {'name': 'Sue', 'age': 34, 'city': 'NYC'},
         {'name': 'Mary', 'age': 24, 'city': 'Springfield'},
         {'name': 'Phil', 'age': 55, 'city': 'Stamford'}
         )

for u in users:
    print(u.keys())
    print(u.values())
    name = u.values()[2]
    age = u.values()[1]
    city = u.values()[0]
    print(name, city, age)
    # print('{n} is from {c} and is {a} years old.'.format(n=name, c=city, a=age))
    print('{n} is from {c} and is {a} years old.'.format(c=city, n=name, a=age))

    print('------------------------------------------------------')

print('-------------------------------------------------------')
