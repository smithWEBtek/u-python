import random


# def rand_num(low, high, n):
#     count = 0
#     while count < n:
#         yield(random.randint(low, high))
#         count += 1


# for num in rand_num(1, 10, 12):
#     print(num)

def rand_num(low, high, n):
    for x in range(n):
        yield(random.randint(low, high))


for num in rand_num(1, 10, 12):
    print(num)
