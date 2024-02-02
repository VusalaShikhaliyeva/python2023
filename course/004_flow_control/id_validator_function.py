def ask_for_id():
    global id_code
    while True:
        user_id = input("Enter an ID: ")
        if user_id.lower() == 'exit':
            print('Good bye!')
            exit()
        try:
            int(user_id)
            if len(user_id) == 11:
                print("Good", user_id)
            else:
                raise Exception
        except ValueError:
            print('ID must be numeric. Try again or type "exit".')
            continue
        except Exception:
            if len(user_id) < 11:
                print('ID is too short')
            else:
                print('ID is too long')
            continue
        else:
            id_code = user_id
    menu()



def menu():
    while True:
        user_choice = input('1.Gender\n'
                            '2.Date of birth\n'
                            '3. Region of birth\n'
                            '4. Validation\n'
                            '5. Change ID\n'
                            '0. Exit\n'
                            '-->')
        if user_choice == '1':
            get_gender()
            continue
        elif user_choice == '2':
            get_birthdate()
            continue
        elif user_choice == '3':
            get_region()
            continue
        elif user_choice == '4':
            validate()
            continue
        elif user_choice == '5':
            break  # stop this cycle
        elif user_choice == '0':
            quit()  # stop program or the same exit ()
        else:
            print('Choice is out of range.')
    ask_for_id()

def get_gender():
    if id_code[0] not in '09':
        if int(id_code[0]) % 2 == 0:
            print('You are Female')
        else:
            print('You are Male')
    else:
        print('There is something wrong with your ID!')


def get_birthdate():
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

def get_region():
    region_num = id_code[7:10]
    if int(region_num) in range(1, 11):
        print('You were born in Kuressaare Hospital')
    elif region_num >= '011' and region_num <= '019':
        print('You were born in Tartu University Women Clinic')
    elif '021' <= region_num <= '150':
        print('You were born in East Tallinn Central Hospital')
    else:
        print("You were not  born in Estonia.")

def validation_process(check):
    result = 0
    for i in range(10):
        result += int(idcode[i]) * check[i]
    return  result % 11
def validate():
    check1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    check2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    result = 0
    if validation_process(check1) == int(id_code[-1]):
        print('ID is valid')
    elif validation_process(check2) == 10:
        if validation_process(check2) == int(id_code[-1]):
            print('ID is valid 2')
        else:
            print('ID is not valid 2')
    else:
        print('ID is not valid')


id_code = ''

