import re
from binarytree import BinarySearchTree, BinaryTreeNode

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
    route_numbers_array = re.sub(r'\+', "", route_numbers).split('\n')
    route_numbers_array.pop()
    return route_numbers_array

def look_up(phone_number, routes_prices_dict):
    while len(phone_number) > 1:
        if routes_cost_tree(contains):
            return routes_prices_dict[phone_number]
        
        phone_number = phone_number[0:-1]
    
    return 0

def routes_tree(routes_array):
    routes_cost_tree = BinarySearchTree()
    prefix, price = route.split(',')
    routes_cost_tree.insert((prefix, price))


def test_call_router():
    phone_numbers_file = './CallRoutingFiles/phone-numbers-10000.txt'
    routes_file = './CallRoutingFiles/route-costs-10000000.txt'
    phone_number_array = phone_numbers(phone_numbers_file)
    route_numbers_array = routes(routes_file)

    file2 = open('phone-numbers-10000-test-scenario2.txt',"w")
    for number in phone_number_array:
        cost = look_up(number, routes_cost)
        file2.write(number + ':' + str(cost) + ',')
    
    file2.close()