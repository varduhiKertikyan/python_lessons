def get_name_address():
    print(input("Type name your name and address: "))
#get_name_address()

def greetings():
    name = input("Type your name: ")
    print(f"Hi {name}")
#greetings()

def room_area():
    width = float(input("Type width of room: "))
    length = float(input("Type lenght of room: "))
    area = width * length
    print(f'Area of room is {area}')
#room_area()

def area():
    width = float(input("Type width in pound: "))
    length = float(input("Type lenght in pound: "))
    area = (width * length)/43560
    print(f'Area is {area} in acres')
#area()

def price_bottles():
    count_smaller_bottle = int(input("How many <=1 litre bottle do you have: "))
    count_bigger_bottle = int(input("How many >1 litre bottle do you have: "))
    print(f"You get ${(count_smaller_bottle * 0.10 + count_bigger_bottle * 0.25, 2)}")
#price_bottles()

def get_bill():
    order = float(input("Type initial order price: "))
    taxes = order * 18 / 100
    tips = order * 20 / 100
    print(f"your bill is {order + taxes + tips}")
#get_bill()

def sum():
    number = int(input("Type interger: "))
    sum = 0
    while number:
        sum += number
        number -= 1
    print(f"sum of numbers is {sum}")
#sum()

def mid():
    sum = 0
    count = 0
    while 1:
        typed_number = int(input("type number: "))
        if typed_number == 0:
            print("0 is ending signal")
            if count != 0:
                print(f"mid number is {sum /count}")
                return
            return
        else:
            sum += typed_number
            count += 1
#mid()

def fizz_buzz():
    n = int(input("type n fot fizz buzz: "))
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            print("fizz buzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
        i += 1
#fizz_buzz()













