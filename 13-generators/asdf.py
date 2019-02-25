# def create_cubes(n):
#     result = []
#     for x in range(n):
#         result.append(x**3)
#     return result


# for x in create_cubes(10):
#     print(x)

def create_cubes(n):
    for x in range(n):
        yield x**3


def get_list(n):
    for x in create_cubes(n):
        print(x)


# get_list(10)
# print(create_cubes(10))
print(list(create_cubes(10)))
