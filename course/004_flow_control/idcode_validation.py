while True:
    id_code = input("Enter an ID: ")
    if id_code.lower() == 'exit':
        print('Good bye!')
        break
    try:
        int(id_code)
        if len(id_code) == 11:
            print("Good", id_code)
        else:
            raise Exception
    except ValueError:
        print('ID must be numeric. Try again or type "exit".')
        continue
    except Exception:
        if len(id_code) < 11:
            print('ID is too short')
        else:
            print('ID is too long')
        continue
    else:
        while True:
            user_choice = input('1.Gender\n'
                                '2.Date of birth\n'
                                '3. Region of birth\n'
                                '4. Validation\n'
                                '5. Change ID\n'
                                '0. Exit\n'
                                '-->')
            if user_choice == '1':
                if id_code[0] not in '09':
                    if int(id_code[0]) % 2 == 0:
                        print('You are Female')
                    else:
                        print('You are Male')
                else:
                    print('There is something wrong with your ID!')
            elif user_choice == '2':
                if id_code[0] not in '09':
                    birth_year = ''
                    if id_code[0] in '12':
                        birth_year = '18'
                    elif id_code[0] in '34':
                            birth_year = '19'
                    elif id_code[0] in '56':
                            birth_year = '20'
                    elif id_code[0] in '78':
                            birth_year = '21'
                    birth_date = f'{id_code[5:7]}.{id_code[3:5]}.{birth_year}{id_code[1:3]}'
                    print(f'Birth Date: {birth_date}')
                else:
                    print('There is something wrong with your ID!')
            elif user_choice == '3':
                region_num = id_code[7:10]
                if int(region_num) in range(1, 11):
                    print('You were born in Kuressaare Hospital')
                elif region_num >= '011' and region_num <= '019':
                    print('You were born in Tartu University Women Clinic')
                elif '021' <= region_num <= '150':
                    print('You were born in East Tallinn Central Hospital')
                else:
                    print("You were not  born in Estonia.")
            elif user_choice == '4':
                check1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
                check2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
                result = 0
                for index in range(10):
                    result += int(id_code[index]) * check1[index]
                if result % 11 == int(id_code[-1]):
                    print('ID is valid')
                elif result % 11 == 10:
                    result = 0
                    for index in range(10):
                        result += int(id_code[index]) * check2[index]
                    if result % 11 == int(id_code[-1]):
                        print('ID is valid 2')
                    else:
                        print('ID is not valid 2')
                else:
                    print('ID is not valid')
            elif user_choice == '5':
                break  # stop this cycle
            elif user_choice == '0':
                quit()  # stop program or the same exit ()
            else:
                print('Choice is out of range.')
