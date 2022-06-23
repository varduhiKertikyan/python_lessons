def fib(n):
    if n in (1, 2):
        return n - 1
    return fib(n - 1) + fib(n - 2)