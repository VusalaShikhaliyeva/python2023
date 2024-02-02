
# empty = {}
empty = dict()
print(type(empty))
print(type(empty))

# dictionaries contains keys or names and values. keys can be strings,
# integer and floats, values can be pretty much everything
# keys must be unique

mix = {'name': 'Roman',
       'age': 35,
       'courses': ['Math', 'Art'],
       'personal_data': {'height': 179, "weight": 95},
       1: 'Hello world!',
       True: "Hello Planet!",  # try not use booleans
       'age2': 35
       }

print(mix)
print(len(mix))

# indexing in dictionaries been done by keys. dictionaries can not be sliced
print(mix["name"])
print(mix.get('123123123'))
print(mix.get("surname", "There is no any information on this"))

# adding and changing the keys within dictionaries
mix['name'] = 'Jack'
mix['phone'] = '555-555-5555'
print(mix)

# changing multiple keys within dictionary
new = {'new':'Simon', 'age': 25, 'address': 'Tartu mnt. 18'}
mix.update(new)
print(mix)

print(mix.get('courses')[1].upper())

# removing from the dictionaries
del mix['name']
print(mix)

age = mix.pop('age')  # pop is storing the value only
age2 = mix.popitem()  # remembers the last item within the dictionary
print(mix)
print(age)
print(age2)

print(list(mix))  # converting dictionaries into integers is not good
print(mix.keys())
print(mix.values())
print(mix.items())
