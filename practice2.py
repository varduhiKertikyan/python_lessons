def unique_words():
    word_list = []
    while 1:
        typed_word = input("type a word: ")
        if typed_word == "":
            break
        else:
            word_list.append(typed_word)
    unique_word_list = []
    for word in word_list:
        if word not in unique_word_list:
            unique_word_list.append(word)
    for unique in unique_word_list:
       print(unique)

#unique_words()

def is_divisor(a, b):
    return a % b == 0

def num_divisors(n):
    divisors = 1
    while divisors <= n:
        if is_divisor(n, divisors):
            print(divisors)
        divisors += 1

def num_divisors2(n):
    return [i for i in range(1, n) if n % i == 0]

#num_divisors(53)
#print(num_divisors2(10))

def is_number_complete(n):
    divisors = 1
    sum = 0;
    while divisors < n:
        if is_divisor(n, divisors):
            sum += divisors
        divisors += 1
    if sum == n:
        return True
    return False

#print(is_number_complete(28))

def zip(data1, data2):
    new_list = [None] * len(data1)
    for i in range(len(data1)):
        new_list[i] = [data1[i], data2[i]]
    return new_list

#print(zip([1, 2, 3, 4], [10, 20, 30, 40]))

def delete_punctution(str):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for s in str:
        if s in punc:
            str = str.replace(s, "")
    return str

#print(delete_punctution("!everv weew@ dg, fhek?"))

def is_palindrome1(str):
     str = delete_punctution(str).lower()
     return str == str[::-1]


#print(is_palindrome1("Dcc bab, ccd"))

def input_numbers():
    while True:
        if not int(input("type number: ")):
            return

#input_numbers()