import re
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
abc
example*com
exampledcom
example.company
ball mall hall wall tall
привет
800-123-123123123
'''

sentence = 'Start a sentence and then bring it to an end'

emails = '''
SampleMaiL@example.com
john.sample@my-work.net
jack-125-production@colledge.edu
bob.Samples@example.co.uk
example@example.org
'''

urls = '''
https://www.google.com
http://www.wordpress.org
https://www.nasa.gov
https://example.net
www.example.net
example.net
'''

print(r'\tTab\n\n\n\t\n')

# pattern = re.compile(r'abc')   # regular expression
# print(pattern)
#
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)
#     # print(match.start())
#     # print(match.end())
#     # print(match.group())

# pattern = re.compile(r'\.') # to find all the symbols just "." for only dots "\."
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

# pattern = re.compile(r'\BHa') # to find all the symbols which includes Ha both middle and ending
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)
#
# pattern = re.compile(r'^Start')  # checks if sting starts with this or not
# matches = pattern.finditer(sentence)
# for match in matches:
#     print(match)

# Numbers
# pattern = re.compile(r'\b\d\d\d.\d\d\d.\d\d\d\b')  # checks the numbers within text with any kind of character within
#
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)
#
# pattern = re.compile(r'\b\d\d\d[.-]\d\d\d[.-]\d\d\d\b')  # checks only the characters within list
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)
#
# pattern = re.compile(r'\b[89]00[.-]\d\d\d[.-]\d\d\d\d\b')  # checks the numbers with starts with 800 or 900
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)
#
# pattern = re.compile(r'[^w]all')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)
#
# pattern = re.compile(r'\b[89]00[.-]\d{3}[.-]\d{1,4}\b')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

# M, Mr Mrs Ms
# pattern = re.compile(r'M(r|s|rs)\.? [A-Z][a-z]*')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)


# urls
#pattern = re.compile(r'(http://|https://)?(www\.)?(\w+)\.([\w.]+)')
# matches = pattern.finditer(urls)
# for match in matches:
#     print(match.group(3))

pattern = re.compile(r'\b[89]00[.-]\d{3}[.-]\d{1,4}\b')
match = pattern.match(text_to_search)  # works only the string starts with the pattern

