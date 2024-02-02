# import itertools as it
#
# counter = it.count()
#
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
#
# data1 = [100, 200, 300, 400]
# data2 = ['abc', 'def', 'ghi', 'jkl', 'mno', 'prs']
#
# data = list(zip(data1, data2))
# print(data)
#
import itertools

import itertools as it

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]

# order = false, reuse_value = false
result = it.combinations(letters, 3)

for line in result:
    print(line)

# order = true, reuse_value = false
result1 = it.permutations(letters, 3)

for line in result1:
    print(line)

# order = true, reuse_value = true
result2 = it.product(letters, numbers, repeat=4)

for line in result2:
    print(line)

# order = false, reuse_value = true
result3 = it.combinations_with_replacement(letters, 4)

for line in result3:
    print(line)

numbers2 = [4, 5, 4, 3, 2, 1, 0, 4]
selectors = [True, False, False, True]

result4 = it.compress(letters, numbers)

print(list(result4))

result5 = filter(lambda x: x % 2, numbers2)
print(list(result5))

result6 = it.dropwhile(lambda x: x > 2, numbers2)
print(list(result6))

result7 = it.takewhile(lambda x: x > 2, numbers2)
print(list(result7))

result8 = it.accumulate(numbers2)
print(list(result8))

def get_city(person):
    return person['city']

people = [
    {
        'name': 'Jack',
        'city': 'Tallinn'
    },
    {
        'name': 'Sarah',
        'city': 'Tallinn'
    },
    {
        'name': 'Bob',
        'city': 'Tallinn'
    },
    {
        'name': 'Sarah',
        'city': 'London'
    },
    {
        'name': 'Mary',
        'city': 'London'
    },
    {
        'name': 'Jane',
        'city': 'Tallinn'
    },
]

people.sort(key=lambda x: x['city'])
result9 = itertools.groupby(people, get_city)

for x in result9:
    print(x)
    print(list(x[1]))

copy = it.tee(result9)
print(list(copy))
