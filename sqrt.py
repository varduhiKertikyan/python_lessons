def sqrt(n):
    root = 1
    while not guess_enough(root, n):
        root = improve(root, n)
    return root

def guess_enough(root, target):
    if abs(root ** 2 - target) < 0.0001:
        return True
    return False

def improve(root, target):
    return (root + (target/root))/2

print(sqrt(25))