def is_divisor(a, b):
    return a % b == 0

def find_smallest_divisor(a, b):
    if is_divisor(a, b):
        return b
    else:
        return find_smallest_divisor(a, b + 1)

def is_prime(n):
    return find_smallest_divisor(n, 2) == n