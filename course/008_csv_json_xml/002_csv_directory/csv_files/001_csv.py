# import csv
#
# with open('test-2.csv', 'r', encoding='utf8') as file:
#     csv_list = csv.reader(file)
#     # print(csv_list) #  iterator
#     with open('test_copy.csv', 'w', encoding='utf8') as wfile:
#         csv_writer = csv.writer(wfile, delimiter='*', lineterminator='\n')
#         # columns = next(csv_list)  # if you use iterator once, it disappears you can't use next with lits
#         for line in csv_list:
#             # print(f'Hello {line[0]}')
#             # csv_writer.writerow(line) # adds a black line automatically
#             csv_writer.writerows(csv_list)
#
# with open('test_copy.csv', 'r', encoding='utf8') as file:
#     csv_data = list(csv.reader(file, delimiter="*"))
#     print(csv_data)
#     for line in file:
#         print(file)
import csv

with open('test-2.csv', 'r', encoding='utf8') as file:
    csv_list = csv.DictReader(file, fieldnames=['Name', 'Birth', 'Town'])   # You should have column names while using DictReader
    print(list(csv_list))
    with open('test_copy.csv', 'w', encoding='utf8') as wfile:
        csv_writer = csv.DictWriter(wfile, delimiter='*', lineterminator='\n', fieldnames=['Name', 'Birth', 'Town'])
    #     # columns = next(csv_list)  # if you use iterator once, it disappears you can't use next with lits
        csv_writer.writeheader()
        for line in csv_list:
    #         # print(f'Hello {line[0]}')
            csv_writer.writerow(line)   # adds a black line automatically
            # csv_writer.writerows(csv_list)
