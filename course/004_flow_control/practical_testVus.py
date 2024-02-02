# 1. Write a program that prompts for the user's first name,
# last name, and age, then outputs a string like: "Hello, <Last Name> <First Name>. Your age is: <Age>."

import math

name = input('Enter your name: ')
surname = input('Enter your surname: ')
age = input('Enter your age: ')

print('Hello, ' + surname.capitalize() + " " + name.capitalize() + '. Your age is: ' + age + ".")

# 2. Write a program that finds the length of the hypotenuse for a right-angled triangle given its two cathets.
# (c = sqrt(a * a + b * b))

catheter_a = input('Enter catheter a: ')
catheter_b = input('Enter catheter b: ')
hypotenuse = math.sqrt(float(catheter_a) ** 2 + float(catheter_b) ** 2)
print(hypotenuse)

# 3. User inputs the lengths of three sides of a triangle (a, b, c) [float].
# Write a program to check if the triangle is a right-angled triangle (c**2 = a**2 + b**2).
# 3, 4, 5
hypotenuse2 = input("Enter hypotenuse: ")
if float(hypotenuse2) ** 2 == float(catheter_a) ** 2 + float(catheter_b) ** 2:
    print("Based on the input you have entered the triangle is right-angled.")
else:
    print('The triangle is not right-angled.')

# 4. User inputs an arbitrary list. Write a program that outputs the elements of the list in reverse order.
# arbitrary_list = ['Hello', "I", "am", "an", "arbitrary", "list", "in", "reverse."]
arbitrary_list = input('Enter list items, use "," as a seperator: ').split(', ')
for element in arbitrary_list[::-1]:
    print(element)


# 5. As tuples are immutable, write a program that allows
# adding tuple B to tuple A in a way that tuple B is placed at index 2.
tuple_A = (1, 2, 3, 5, 8)
tuple_B = (8, 2, 5)  # result = (1, 2, 8, 2, 5, 3, 5, 8)
result = tuple_A[:2] + tuple_B + tuple_A[2:]
print(result)

# 6. Write a program that finds the most frequently occurring number(s) in an
# arbitrary list and returns them in a list.
# x = [1, 1, 2, 3, 4, 4, 4] => [4]
# x = [1, 1, 2, 3, 4, 4] => [1, 4]

#x = [1, 1, 2, 3, 4, 4]
x = [1, 1, 2, 3, 4, 4, 4]
max_count = 0
count_element = 0
my_dict = {}

for i in x:
    if count_element > max_count:
        max_count = count_element
    count_element = 0
    for j in x:
        if j == i:
            count_element += 1
    my_dict[i] = count_element

max_list = []
for i in my_dict:
    print(i)
    if my_dict[i] == max_count:
        max_list.append(i)

print(max_list)

# 7. Display the number of seconds as days:hours:minutes:seconds.
#1234566 => 14:6:56:6

total_seconds = input("Please enter the seconds to convert: ")
days = int(total_seconds) // 86400
hours = (int(total_seconds) % 86400) // 3600
minutes = (int(total_seconds) % 3600) // 60
seconds = int(total_seconds) % 60
print("Display " + str(days) + ':' + str(hours) + ':' + str(minutes) + ':' + str(seconds))