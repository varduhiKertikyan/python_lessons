import random

def reverse_number():
    number = int(input("input number: "))
    reversed = 0
    while(number != 0):
        remainder = int(number % 10)
        reversed = reversed * 10 + remainder
        number = int(number / 10)
    return reversed

#print(reverse_number())

def join_tuple_numbers(tuple: tuple):
    number = 0
    length = len(tuple)
    for i in range(1, length):
        number += 10 ** i + tuple[-i] 
    return number

print(join_tuple_numbers((3, 2, 4, 5)))

def sum_of_min_max(data):
    min = data[0]
    max = 0
    for number in data:
        if number > max:
            max = number
        if number < min:
            min = number
    return min + max

#print(sum_of_min_max([10, 2, 5, 30]))

def even_index(data):
    for i in range(len(data)):
        if data[i] % 2 == 0:
            print(i)

#even_index([5, 4, 3, 3, 6])

def reverse_string(str):
    new_str = len(str) * [None]
    for i in range(len(str)):
        new_str[i] = str[-1]
    print(new_str)

#reverse_string("abcd")

def is_divisor(a, b):
    return a % b == 0

def find_smallest_divisor(a, b):
    if is_divisor(a, b):
        return b
    else:
        return find_smallest_divisor(a, b + 1)

def is_prime(n):
    return find_smallest_divisor(n, 2) == n

def smallest_prime(n):
    smallest = n + 1
    while(not is_prime(smallest)):
        smallest =+ 1
    print(smallest)

#smallest_prime(4)

def get_median(data):
    if len(data) % 2 == 0:
        return data[len(data) // 2 - 1], data[len(data) // 2]
    return data[len(data) // 2]

#print(get_median([1, 2, 3, 4, 5, 5, 7, 8]))

def get_mouth_days(year, mouth):
    days = 0
    return days

#get_mouth_days()

def same_parity(n, *args):
    map(is_divisor(*args), n)

#print(same_parity(10, [20, 3, 10]))

def random_passwd(n):
    psw = ""
    for i in range(n):
        symbol = random.randint(33, 126)
        psw += chr(symbol)
    return psw

#print(random_passwd(10))













