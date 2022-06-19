def triple(data):
    return data*3

def map(triple, list):

    ''' returns a list of triple data members'''

    new_list = [None] * len(list)
    for i in range(len(list)):
        new_list[i] = triple(list[i])
    return new_list


#function call
list = [3, 4, 2, 7, 8, 20]
print(map(triple, list))