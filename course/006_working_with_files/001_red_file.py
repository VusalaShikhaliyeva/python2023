# # 'r' = read
# # 'w' = write
# # 'x' = create
# # 'a' = append
# # 'r+' = read and write
#
# # /Users/vusalashikhaliyeva/PycharmProjects/python2023/course/006_working_with_files/001_red_file.py
# # course/006_working_with_files/001_re.d_file.py
#
# # file = open('text_files/lorem.txt', 'r', encoding='cp1253')
# # print(file.name)
# # print(file.mode)
# #
# # with open('text_files/lorem.txt', 'r', encoding='utf8') as file:
# #     print(file.closed)
# #
# # print(file.closed)
# #
# # print(len(data))
# # print(len(data[0]))
# # readline() - reading the text line by line
# # file.readline(10) - reading the first 10 characters of the first line
#
# with open('text_files/lorem_copy.txt', 'w', encoding='utf8') as file:
#     file.write('*******\n')
#    # pass  # cleans the file is only pass is in the code
#     file.write("Hello Python!\n")
#     for num in range(10):
#         if num ** 2 > 50 :
#             file.write(f'{num} => {num ** 2} BIGGER\n')
#         else:
#             file.write(f'{num} => {num ** 2} SMALLER\n')
#
# with open('text_files/lorem_copy.txt', 'a', encoding='utf8') as file:
#     file.write('*******\n')
#    # pass  # cleans the file is only pass is in the code
#     file.write("Hello Python!\n")
#     for num in range(10):
#         if num ** 2 > 50 :
#             file.write(f'{num} => {num ** 2} BIGGER\n')
#         else:
#             file.write(f'{num} => {num ** 2} SMALLER\n')

with open(