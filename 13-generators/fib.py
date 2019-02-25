def fib(n):
    a = 1
    b = 1
    for i in range(n):
        yield(a)
        a, b = b, a+b


for num in fib(9):
    print(num)
