def pascal(m, n):
    return 1 if n in (m, 1) else pascal(m - 1, n) + pascal(m - 1, n - 1)

print(pascal(3, 3))
