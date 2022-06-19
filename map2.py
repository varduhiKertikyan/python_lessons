def pow(base, exp):
    return base ** exp

def map2(func, data1, data2):

    ''' map function which returns a list applying func function'''

    new_list = [None] * len(data1)
    for i in range(len(data1)):
        new_list[i] = func(data1[i], data2[i])
    return new_list


#function call
print(map2(pow, [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))