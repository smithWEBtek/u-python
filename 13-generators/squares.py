def gensquares(N):
    for x in range(N):
        yield(x*x)

for x in gensquares(10):
    print(x)
