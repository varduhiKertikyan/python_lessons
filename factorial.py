def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

def fact2(n):
    res = 1
    prod = 1
    while prod <= n:
        res *= prod
        prod += 1
    return res

def fact(n, res):
    if n == 1:
        return res
    return fact(n - 1, res * n)