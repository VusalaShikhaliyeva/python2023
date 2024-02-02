cars = [
    {
    'car': 'Honda',
    'model': 'Civic',
    'milage': 10000,
    'color': 'red'
    },
    {
    'car': 'BMW',
    'model': '328i',
    'milage': 170000,
    'color': 'white'
    },
    {
    'car': 'Audi',
    'model': 'A6',
    'milage': 24000,
    'color': 'black'
    }
]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = map(lambda x: [x, x ** 2, x**3], numbers)  # map returns modified lists
print(list(squares))

def change_cars(car):
    return {
       f"{car['car']} {car ['model']}": {
           'mileage': car['milage'],
           'color': car['color']
       }
    }

new_cars = map(change_cars, cars)
print(list(new_cars))

# numbers
def even(num):
    return not num % 2
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = filter(even, numbers2)
print(list(even_numbers))