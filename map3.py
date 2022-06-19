def sum(num1, num2, num3):
    return num1 + num2 + num3

def map3(func, data1, data2, data3):

    ''' map function which returns a list applying func function'''

    new_list = [None] * len(data1)
    for i in range(len(data1)):
        new_list[i] = func(data1[i], data2[i], data3[i])
    return new_list


#function call
print(map3(sum, [1, 2, 3], [10, 20, 30], [100, 200, 300]))