# mylist = [1, 2, 2, 3]
# mylist.pop()
# print(mylist)

# # mylist.insert
# # help(mylist.insert)
# # append
# # count
# # extend
# # insert
# # pop
# # remove
# # reverse
# # sort


# def say_hello(arg):
#     '''
#     DOCSTRING: Information about the function
#     INPUT: no input
#     OUTPUT: Hello
#     '''
#     print(f'Hello {arg}')


# def greeting(name):
#     print('Hello %s' % (name))


# say_hello('Frank')
# say_hello('Milo')
# greeting('Frank')
# greeting('Milo')


# def add_nums(n1, n2):
#     return n1 + n2


# print(add_nums(9, 3))


# def lesser_of_two_evens(a, b):
#        if a % 2 == 0 and b % 2 == 0:
#             return list([a, b]).sort()[0]
#         elif a % 2 != 0 and b % 2 != 0:
#             return list([a, b]).sort()[1]
#         else:
#             return None


# print(lesser_of_two_evens(2, 4))
# print(lesser_of_two_evens(2, 5))
# print(lesser_of_two_evens(6, 12))

# def dog_check(phrase):
#     return 'dog' in phrase.lower()
# print(dog_check("My Dog ran away."))

# def pig_latin(word):
#     # if word[0].lower() in 'aeiou':
#     #     pig_word = word + 'ay'
#     #     print(pig_word)
#     #     return pig_word
#     if word[1].lower() in 'aeiou':
#         pig_word = word[1:] + word[0] + 'ay'
#         return pig_word

# def pig_latin(word):
#     first_letter = word[0]
#     if first_letter in 'aeiou':
#         pig_word = word + 'ay'
#     else:
#         pig_word = word[1:] + first_letter + 'ay'
#     print(pig_word)
#     return pig_word


# pig_latin('apple')
# pig_latin('adam')
# pig_latin('ezra')
# pig_latin('idle')
# pig_latin('ralph')
# pig_latin('tim')
# pig_latin('bob')
# pig_latin('jeff')


# def dog_check(phrase):
#     if 'dog' in phrase:
#         print('yes it has dog')
#         return True
#     else:
#         print('no it does not have dog')
#         return False

# def dog_check(phrase):
#     return 'dog' in phrase.lower()


# print(dog_check("My dog ran away."))
# print(dog_check("My cat ran away."))
# print(dog_check("My Dog ran away."))


# def lesser_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min(a, b)
#     else:
#         return max(a, b)


# lesser_of_two_evens(2, 4)

# def print_big(letter):
#     patterns = {1: '  *  ', 2: ' * * ', 3: '*   *', 4: '*****',
#                 5: '**** ', 6: '   * ', 7: ' *   ', 8: '*   * ', 9: '*    '}
#     alphabet = {'A': [1, 2, 4, 3, 3], 'B': [5, 3, 5, 3, 5], 'C': [
#         4, 9, 9, 9, 4], 'D': [5, 3, 3, 3, 5], 'E': [4, 9, 4, 9, 4]}
#     for pattern in alphabet[letter.upper()]:
#         print(patterns[pattern])


# print_big('a')
# print_big('b')
# print_big('c')
# print_big('d')
