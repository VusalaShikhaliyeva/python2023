id_code = input('Please enter your id: ')

if len(id_code) == 11:
    print('Correct!', id_code)
elif len(id_code) > 11:
    print('Incorrect! ID code is too long!')
else:
    print('Incorrect! ID code is short.')

# nested if
if len(id_code) == 11:
    print('Correct!', id_code)
else:
    if len(id_code) > 11:
        print('Incorrect! ID code is too long!')
    else:
        print('Incorrect! ID code is short.')


x = "HELLO WORLD"
if x.isupper():
    print(x.lower())
else:
    print(x.upper())

if x:
    print(x)
else:
    print("Nothing")

x = input('Enter your name!')
if x:
    print('Hello', x)
else:
    print('You didnot enter a name!')

x = input('Enter your name!')
y = input('Enter your surname!')
if x and not y:
    print('Hello', x)
elif x and y:
    print('Hello', x, y)
else:
    print('You didnot enter a name!')
