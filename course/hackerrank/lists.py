def print_full_name(first, last):
    if len(first_name) <= 10 & len(last_name) <= 10:
        print(f'Hello {first_name} {last_name}! You just delved into python.')
    else:
        print(f'Name and Surname length should be less or equal to 10.')

first_name = input()
last_name = input()
print_full_name(first_name, last_name)