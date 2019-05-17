# Linear Solution

import re

def phone_numbers(phone_numbers_file):
    ''' Turns phone #'s into array and removes + sign'''
    file = open(phone_numbers_file, 'r')
    phone_numbers = file.read()
    file.close()
    phone_numbers_array = re.sub(r'\+', "", phone_numbers).split('\n')
    phone_numbers_array.pop()
    return phone_numbers_array

def routes(routes_file):
    file = open(routes_file)
    route_numbers = file.read()
    file.close
    prefix_array = []
    price_array = []
    route_numbers_array = re.sub(r'\+', "", route_numbers).split('\n')
    route_numbers_array.pop()
    for route in route_numbers_array:
        prefix, price = route.split(',')
        prefix_array.append(prefix)
        price_array.append(price)
    print(prefix_array)
    print(price_array)
    return route_numbers_array

def look_up(phone_number, prefix_array):
    while len(phone_number) > 1:
        for prefix in prefix_array:
            if phone_number == prefix:
                return prefix_array.index(prefix)
        
        phone_number = phone_number[0:-1]
    
    return 0


def test_call_router():
    phone_numbers_file = './CallRoutingFiles/phone-numbers-1000.txt'
    routes_file = './CallRoutingFiles/route-costs-106000.txt'
    phone_number_array = phone_numbers(phone_numbers_file)
    route_numbers_array = routes(routes_file)
    
    prefix_array = []
    price_array = []
    for route in route_numbers_array:
        prefix, price = route.split(',')
        prefix_array.append(prefix)
        price_array.append(price)
    file2 = open('phone-numbers-1000-test-scenario2.txt',"w")
    for number in phone_number_array:
        index = look_up(number, prefix_array)
        cost = price_array[index]
        file2.write(number + ':' + str(cost) + ',')
    
    file2.close()

test_call_router()