# def no_params():
#     # print('Hello world!')
#     return 'Hello Planet!'
#
# print('Part1')
# no_params()  # functions are reusable
# print('Part2')
# print(no_params())  # function is equal to what it returns
#
#
# def square_area(width, height):
#     result = width * height
#     return result
#
# print(square_area(10, 20))
# print(square_area(5, 20))
# print(square_area(50, 5))
#
#
# # def say_hello() -> object:
# #     print(f'Hello! {name}!')
#
# def say_hi():
#     name = input('Enter name: ')
#     print(f'Hi {name}!')
#
# say_hi()
#
# a = 1
# b = 2
# c = 3
#
# def something():
#     a = 10
#     b = 20
#     print('LOCAL', a, b, c)
#
# something()
# print('GLOBAL', a, b, c)
#
# names = []
# number = 1
# def add_name(name):
#     global number
#     names.append(name)
#     number += 1  # you cannot assign new a value to global variable in Local unless you add global
#
# add_name('Jack')
# add_name('Sara')
# add_name('Bob')
# add_name('Vus')
# print(names, number)
#
# def sample(a, b, c=0):
#     print(a + b + c)
#
# sample(1, 2, 3)
#
# def personal_data(data):
#     name = data[0]
#     surname = data[1]
#     age = data[2]
#     print(f'Hello {name} {surname}')
#
# personal_data(["Jack", "Smith", 25])

def sum_many_numbers(num1, num2, *args, **kwargs):  # args is all the additional data we use within it.

    result = num1 + num2
    for num in args:
        result += num

    print(kwargs)
    return result

print(sum_many_numbers(20, 30, 2, 3, 4, 5, 6, 7, 89, 91, 23, 34, 45, 56, 67, 799, 1000, name = 'Jack', surname = 'Smith'))

# x = (1, 2, 3)
# y = (10, *x, 20, 30)
# print(y)

def area(a, b):
    return a * b

def perimeter(a, b):
    return (a + b) * 2

def count_material(amount, a, b):
    area_material = area(a, b) * amount
    edge_material = perimeter(a, b) * amount
    return {'total area': area_material, "total_edge" : edge_material}

print(count_material(10, 20, 40))