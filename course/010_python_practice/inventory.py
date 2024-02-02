# Inventory Management app
# Product - name(key), {quantity, price}(value)
# Functions
# add item
# remove item
# update price
# sell item
# display inventory
# calculate total value

inventory = {'Apple': {'quantity': 7, 'price': 0.5}, 'Orange': {'quantity': 10, 'price': 0.7}}
def add_product(name, quantity, price):
    if name in inventory:
        print(f'{quantity} {name}s were added')
        inventory[name]['quantity'] += quantity
    else:
        inventory[name] = {"quantity": quantity, "price":price}
        print(f'{name}s were added to inventory')


def remove_product(name):
    if name in inventory:
        del inventory[name]
        print(f'{name} was deleted')
    else:
        print(f'{name} is not in inventory')

# remove_product("Orange")
def update_price(name, price):
    if name in inventory:
        inventory[name]["price"] =  price
        print(f'Price for {name} updated to ${price:.2f}')
    else:
        print(f'{name} is not in the inventory')

# update_price("Orange", 1)
print(inventory)

def sell_product(name, quantity):
    if name in inventory:
        if inventory[name]["quantity"] >= quantity:
            inventory[name]["quantity"] -=quantity
            total_price = inventory[name]['price'] * quantity
            print(f'{quantity} {name}s were sold. Total: ${total_price:.2f}')
        else:
            print(f'Not enough {name} in stock. There are only {inventory[name]["quantity"]} {name}s left!.')
    else:
        print(f'{name} is not in the inventory')

# display inventory
# def display_inventory():
#     for product in inventory:
#         print(f'{product} - qty:{inventory[product]["quantity"]}, price:${inventory[product]['price ']:.2f}')

def display_inventory():
    for product, data in inventory.items():
        print(f'{product} - qty:{data["quantity"]}, price:${data['price']:.2f} ')
display_inventory()

# def calculate_total_value():
#     total_price = 0
#     for product, data in inventory.items():
#         total_price += (data["quantity"] * data["price"])
#         print(f'Total price of the inventory: {total_price}.')

def calculate_total_value():
    total_value = 0
    for data in inventory.values():
        total_value += data['quantity'] * data['price']
    print(f'Total price of the inventory: {total_value}.')

calculate_total_value()

