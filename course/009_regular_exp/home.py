# 1. Write a regular expression to find an HTML color specified as #ABCDEF, meaning # followed by 6 hexadecimal characters.
# Color hashes use values from 0 to 15, where 0-9 are digits from zero to nine, and 10-15 are letters from A-F.
#
# 2. Find the time in the text. The time has the format hours:minutes. Both hours and minutes consist of two digits, for example, 09:00. Write a regular expression to find the time in the string: "Breakfast at 09:00". Note that "37:98" is an incorrect time. [00:00 - 23:59], 232:23 23:312 123:123
#
# 3. Write a program that will extract from the file people.txt:
# All names and surnames
# All addresses
#
# 4.Write a regular expression to check a string, the task is to determine if the string consists of characters a-z, A-Z, 0-9.
#
# 5. Write a regular expression to determine the Estonian personal identification code (isikukood).

import re

text1 = '#121212, #NNGGSS, #0099562213, #AA0012'
pattern1 = re.compile(r'#[\b0-9A-Fa-f]{6}\b')

matches1 = pattern1.finditer(text1)
for match in matches1:
    print(match)

text2 = '23:19, 234:40, 25:39, 15:61, 00:00, 23:59, 01:43, 20:99'
pattern2 = re.compile(r'\b([01]\d|2[0-3]):[0-5][0-9]\b')

matches2 = pattern2.finditer(text2)
for match2 in matches2:
    print(match2)

with open('people.txt', 'r', encoding='utf8') as file:
    data = file.read()

people_ptrn = re.compile(r'[A-Za-z-]+ [A-Za-z-]+')

people_matches = list(people_ptrn.finditer(data))
print(len(people_matches))
for person in people_matches:
    print(person)

address_ptrn = re.compile(r'\d{3} [A-Za-z]+ St\., [A-Za-z- ]+ [A-Z]{2} \d{5}]')
address_matches = list(address_ptrn.finditer(data))
print(len(address_matches))
for address in address_matches:
    print(address)

text3 = 'Hello people!'

pattern3 = re.compile(r'[^A-Za-z0-9]')
matches3 = pattern3.finditer(text3)
for match3 in matches3:
    print(match3)

matches3 = list(pattern3.finditer(text3))
if len(matches3) != len(text3):
    print('FALSE')
else:
    print('TRUE')

pattern4 = re.compile(r'\b[1-8]\d{2}(0[1-9]|1[0-2])(0[0-9]|[12]\d|3[01])\d{4}\b')
