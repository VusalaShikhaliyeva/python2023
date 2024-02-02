x = "hello"
# y = int(x)  # critical error - nothing after this line will work

number = input('Enter number: ')
# print(int(number) ** 2)

# print('DIGIT', number.isdigit())
# print('DECIMAL', number.isdecimal())

try:
    print(int(number) ** 2)
except ValueError:
    print(number, "is not a number!")  # except is compulsory in try except flow control


try:  # checks code for critical errors
    result = int(number) ** 2
    int(number) / 0
except ValueError:
    print(number, "is not a number!")  # executes in case of error inside try
except ZeroDivisionError:
    print('You are trying to divide by 0.')
else:
    print(result)  # Executes in case of no error inside try
finally:
    print('Good bye')  # executes no matter what

raise ValueError  # creates an error
