# import csv
#
# with open("2019.csv", "r", encoding="utf8") as file:
#    countries_csv = csv.DictReader(file)
#    # print(list(countries_csv))
#    countries = list(countries_csv)
#
# # for i in countries:
# #    print('Overall rank: ' + countries[i])
#
# # print(countries[1].values())
# #
# # for i in range(0, len(countries)):
# #     print(countries[i].values())
#
# # def sort():
# #     for i in range(0, len(countries)):
# #         print(len(countries[i].keys()))
# # print(sort())
# def selected_feature():
#     for i in range(0, len(countries[0].keys())):
#         for j in range(0, len(countries)):
#             print(list(countries[j].values()))
#
# print(selected_feature())
#

import csv

with open("2019.csv", "r", encoding="utf8") as file:
    data = csv.reader(file)
    headers = next(data)
    ###### USING LAMBDA ######
    # data = list(data)
    # data.sort(key=lambda x: x[3], reverse=True)
    # for index in range(10):
    #     print(data[index])

    ###### WITHOUT LAMBDA ######
    # result = []
    # for item in data:
    #     result.append([item[3], item[1]])
    # result.sort(reverse=True)
    # for index in range(10):
    #     print(result[index])

    ###### MENU VERSION ######
    data = list(data)

def get_top(fieldname):
    top = int(input('How many countries? ---> '))
    data.sort(key=lambda x: x[fieldname], reverse=True)
    for index in range(top):
        print(data[index])

def menu():
    while True:
        user_choice = input('1. GDP per capita \n'
                            '2. Social support \n'
                            '3. Healthy life expectancy \n'
                            '4. Freedom to make life choices \n'
                            '5. Generosity \n'
                            '6. Perceptions of corruption \n'
                            '0. Exit \n'
                            '-->')
        if user_choice == "1":
            get_top(3)
        elif user_choice == "2":
            get_top(4)
        elif user_choice == "3":
            get_top(5)
        elif user_choice == "4":
            get_top(6)
        elif user_choice == "5":
            get_top(7)
        elif user_choice == "6":
            get_top(8)
        elif user_choice == "0":
            break
        else:
            print("Chose is out of range! Try again.")

menu()