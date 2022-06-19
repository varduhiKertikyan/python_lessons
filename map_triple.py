def triple(data):
    return data*3

def _map(func, list):

    ''' map function which returns a list applying func function'''

    new_list = [None] * len(list)
    for i in range(len(list)):
        new_list[i] = func(list[i])
    return new_list


#function call
list = [3, 4, 2, 7, 8, 20]
print(_map(triple, list))