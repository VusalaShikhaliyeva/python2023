print('Hello World!')  # this is print statement

'''
this is a long comment 
for the future 
when you will come back to review 
'''


'''Variables 
Variables are used to store the data 

you do not store your data with uppercase letters written variables

you can't start Python variables with numbers. but _variable is acceptable

do not assign the method names to variables
'''

age = 27

my_favourity_food_type = "dolma"  # Python is build with underscores not camel

print(age, age, age, age, my_favourity_food_type)

'''
red errors - critical errors
yellow warning - not PEP standart - for cleaner code
'''

# Data types

print(500)
print(type(500))   # integer

print(500.23)
print(type(500.23))   # float

print(500.0)
print(type(500.0))  # still float

# sum of 2 integers is integer.
print(2 + 3)

# the sum of floats is float
print(0.1 + 0.2)

# the sum of float and integer is float
print(5 + 0.2)

# rounding the numbers
print(round(1.5))

print(round(2.5))

# floats are not exact!

# calculator

num = 432

print(400 + 23.4 + 12)
print(400 - 23.4 - 12)
print(400 - 23.5 - 12 - num)
print(40 * num * 0.5)
print(num / 13)
print(num // 13)  # floor division.  rounding to the floor. it will be integer
print(9.9999 // 1)  # is one of the numbers is float then the result is float
print(10 ** 2)  # exponentation
print(144 ** 0.5)  # root
print(9 % 4)  # the one is left, remainder
print(6 % 2)

# STRING

print('Hello World')
print("Hello Planet")
print(type("hello"))
print(type(''))
print(type('999'))
print('999' + '111')
# print(999 + '999')  # do not do this

# BOOLEAN

print(True)
print(False)
print(type(True))  # bool

print(None)
print(type(None))


name = 'Vus'
print('Hello ' + name)

# Type Conversion

# int, float, str, bool
int_var = 500
float_var = 50.9
string_var_num = '123'
string_var_float ='123.43'
string_var_txt = 'Hello world'
bool_var = False

print(int(float_var))
print(int(string_var_num))
#print(int(string_var_float))  you can't convert float string into integer
print(int(bool_var))

print(float(int_var))
#print(float(string_var_txt))   - error
print(float(string_var_float))   # works here
print(int(float(string_var_float)))
print(float(bool_var))


print(bool(0))
print(bool(string_var_txt))
print(bool(''))
print(bool(' '))


num = 27
text = "Vus"
boolean = False

message = "Hello " + text + '. I am ' + str(num) + ' years old.'
print(message)

# ask user to enter some value
user_age =  input('Please enter your age: ')
print(user_age)
print(type(user_age))  # always string