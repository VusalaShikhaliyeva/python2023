for num in range(1, 101):
    if num % 3 == 0:
        print('FIZZ')
    elif num % 5 == 0:
        print('BUZZ')
    elif num % 3 == 0 and num % 5 ==0:
        print ('FIZZBUZ')
    else:
        print(num)

