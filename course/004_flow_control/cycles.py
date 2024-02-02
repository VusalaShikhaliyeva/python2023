#  iterable

people = ['Jack', 'Mary', 'Sarah', 'Bob']

#loop

for person in people:  # have self-explanatory variable
    print(f'Hello {person}!')

x = list(range(1, 10))
print(x)

for number in range(100):
    print(number ** 2)

for number in range(100):
    if number ** 2 % 2 == 0:
        print(f'{number ** 2} EVEN')
    else:
        print(f'{number ** 2} ODD')

# nested cycle
for num1 in range(10):  # 10 loops
    for num2 in range(10):  # 100 loops
        for num3 in range(10):  # 1000 loops
            for num4 in range(10):  # 1000 loops
                print(num1, num2, num3, num4)

people = [('Jack', 'Smith', 25), ('Mary', 'Gold', 20), ("Sarah", "Summers", 30), ("Bob", 'Green', 40)]

for person in people:
    print(person)
    print(f'Hello {person[0]} {person[1]}. You are {person[2]} years old.')

for name, surname, age in people:
    print(f'Hello {name} {surname}. You are {age} years old.')

people = [('Jack', 'Smith', 25, 'male'),
          ('Mary', 'Gold', 20, 'female'),
          ("Sarah", "Summers", 30, None),
          ("Bob", 'Green', 40, None)]

for name, surname, age, gender in people:
    if gender is None:
        print(f'Hello {name} {surname}.  You are {age} years old.')
    elif gender == "male":
        print(f'Hello {name} {surname}.  You are {age} years old. You are male')
    elif gender == "female":
        print(f'Hello {name} {surname}.  You are {age} years old. You are female')


for name, surname, age, gender in people:
    if gender is None:
        print(f'Hello {name} {surname}.  You are {age} years old.')
    else:
        print(f'Hello {name} {surname}.  You are {age} years old. You are {gender}')

# while True:
#     print('I cannot stop!')

x = 0
while x < 100:
    print(x)
    x += 1

colors = []

condition = True
while condition:
    user_input = input('Enter color or type "exit" to quit: ')
    if user_input.lower() == "exit":
        condition = False
    else:
        colors.append(user_input)
        print(colors)


while condition:
    user_input = input('Enter color or type "exit" to quit: ')
    if user_input.lower() == "exit":
        pass                                # allows to continue to the else
    elif user_input.lower () == "print":
        print(f'Colors: {", ".join(colors)}.')
    else:
        colors.append(user_input)
        print(colors)
        print('END OF WHILE')

while condition:
    user_input = input('Enter color or type "exit" to quit: ')
    if user_input.lower() == "exit":
        break                                # stops the cycle as soon as it reaches here
    elif user_input.lower () == "print":
        print(f'Colors: {", ".join(colors)}.')
    else:
        colors.append(user_input)
        print(colors)
        print('END OF WHILE')

print('Good bye!')

while condition:
    user_input = input('Enter color or type "exit" to quit: ')
    if user_input.lower() == "exit":
        break
    elif user_input.lower () == "print":
        print(f'Colors: {", ".join(colors)}.')
        continue
    else:
        colors.append(user_input)
        print(colors)
        print('END OF WHILE')

while True:
    user_choice = input('Enter a number: ')
    if user_choice == '1':
        user_name = input("Enter your name: ")
        print ('You chose 1')
    elif user_choice == '2':
        print ('You chose 2')
    elif user_choice == '3':
        print ('You chose 3')
    elif user_choice == '4':
        print( 'You chose 4')
    elif user_choice. lower () == 'exit':
        print ('Good bye!')
    break
    else:
        print("Out of range! ")

