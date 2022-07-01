a = [1, 2, 3, 4, 5]
b = [7, 3, 8, 5]
result = [elem for elem in a if elem in b]
#print(result)

#print(int('ABC', 16))

def pascal_triangle(n):
    row = [1]
    y = [0]
    for x in range(max(n, 0)):
        #print(row)
        row = [left + right for left, right in zip(row + y, y + row)]

pascal_triangle(6)


def convert(seconds):
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    #print(f'{days}:{hours}:{minutes}:{seconds}')

convert(1234565)


# values = input('Введите числа через запятую: ')
# ints_as_strings = values.split(',')
#ints = map(int, ints_as_strings)
# ints = (int(ints) for ints in ints_as_strings)
# lst = list(ints)
# tup = tuple(lst)
#print('Список:', lst)
#print('Кортеж:', tup)
#

def get_extension(filename):
    filename_parts = filename.split('.')
    if len(filename_parts) < 2:  # filename has no dots
        raise ValueError('the file has no extension')
    first, *middle, last = filename_parts
    if not last or not first and not middle:
        # example filenames: .filename, filename., file.name.
        raise ValueError('the file has no extension')
    return filename_parts[-1]

#print(get_extension('abc.aaa.kkk.py'))


def solve(n):
    n1 = n
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    #print(n1 + n2 + n3)

solve(5)

a = [1, 2, 3, 4, 3, 5]
b = [8, 2, 3, 8]

def print_for_second(lst1, lst2):
    return [elem for elem in lst1 if elem not in lst2]

#print(print_for_second(a, b))

def sum_digits(num):
    digits = [int(d) for d in str(num)]
    return sum(digits)

#print(sum_digits(5245))

list = [4, 2, 1, 5, 3]
min = list[0]
for i in range(len(list)):
    if list[i] < min:
        min = list[i]
#print(min)



list1 = [5, 10, 15, 20, 25, 50, 20]

index = list1.index(20)
list1[index] = 200
#print(list1)


list = ["1", "2", "3", "", "2", "4"]
new_list = [elem for elem in list if elem not in ""]

print(new_list)

