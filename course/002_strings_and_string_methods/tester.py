string_sample1 = 'Hello world world'
string_sample2 = 'first lEtter is lOwerCase'
string_sample3 = '   ***extra whitespace and stars***    '
german_sample = ' der fluß'

text = "single"\
    "quote"\
     "some"
print(text)

text2 = '''Hello
people
of 
        planet
                     Earth.'''

text3 = 'My favourite book is "Metro 2033".'
print(text3)

# length
print(len(text2))  # length of the string
print(len('hello\''))

# indexing from 0
print(string_sample1[0])  # for the first letter

# slicing the last integer is not included [START : END]
print(string_sample1[6:10])

# every second letter [START: END : STEP]
print(string_sample1[:11:2])

print(string_sample1[-3: -1])

print(string_sample1[::-1])

a = 5
A = 10


print(string_sample2.upper())
string_sample2 = string_sample2.upper()
print(german_sample.lower())
print(german_sample.casefold())
print(german_sample.islower())  # returns boolean



print('hello', end='***')  # end parameter is for string only
print('world', end='###')
print('common')

print('Year', 2023, True, None, sep=',')  # separator by default is space, any mark you set for separator will be sep.

salary = 2000
text = "John's salary is {}"
print(text.format(salary))

name = 'Vus'
text2 = "{}'s salary is {}"
print(text2.format(name, salary))

text3 = "{0}'s salary is {1}. {0} is writing {2} code."
print(text3.format(name, salary, "Python"))


message = 'This {product:} costs {cost:}$.'
print(message.format(product='Computer', cost=1000))

print(f'Hello {name}')  # f is formatting. you can use Python methods here.
print(f'Hello {name.upper()}. {name}s salary is {salary:.2f}.')   # the best version of formatting in creating strings
