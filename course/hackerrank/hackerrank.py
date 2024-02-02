if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

i = 0
j = 0
k = 0

coordinates = []
elements = []

for i in range(0, x + 1):
    for j in range(0, y + 1):
        for k in range(0, z + 1):
            if i + j + k != n:
                elements.append(i)
                elements.append(j)
                elements.append(k)
                coordinates.append(elements)
                elements = []
        k += 1
    j += 1
i += 1

print(coordinates)
