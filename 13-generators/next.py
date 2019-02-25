def simple_gen():
    for x in range(3):
        yield(x)


# for n in simple_gen():
#     print(n)

g = simple_gen()

print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
