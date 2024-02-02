if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

arr = sorted(set(arr), reverse=True)  # set converts list into set removing the duplicants

print(arr[1])