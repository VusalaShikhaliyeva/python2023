x = [1, 1, 2, 3, 4, 4, 5, 5, 5]
#Rx = [1, 1, 2, 3, 4, 4, 4]
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
    if my_dict[i] == max_count:
        max_list.append(i)

print(max_list)
#print(my_dict)
