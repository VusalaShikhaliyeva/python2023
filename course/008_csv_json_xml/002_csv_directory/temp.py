import csv

x = [1, 3, 5, 2, 8, 4]
x.sort()
print(x)

def sorting_list(i):
    return i[1]

y = [[3, 1], [6, 8], [1, 5], [4,4]]
#y.sort(key=sorting_list)
y.sort(key=lambda i: i[1])
print(y)

a = lambda: print('Hello world')  # way of creating short functions
a()

