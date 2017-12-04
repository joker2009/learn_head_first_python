__author__ = 'joker_jiang'

# the_file = open('sketch.txt')
#
# the_file.close()
import os

# file_path = os.getcwd()
# print(file_path)
os.chdir('E:\learn_head_first_python\chapter3')
file_path2 = os.getcwd()
# print(file_path2)
if os.path.exists('sketch.txt'):
    data = open('sketch.txt')
# print(data.readline(), end='')
# print(data.readline(), end='')


# data.seek(0)
# for each_line in data:
#     print(each_line, end='')
# data.close()

# data.seek(0)
# for each_line in data:
#     # print(each_line, end='')
#     (role, line_spoken) = each_line.split(':', 2)
#     print(role, end='')
#     print(' said: ', end='')
#     print(line_spoken, end='')
# data.close()

    for each_line in data:
        # print(each_line, end='')

        try:

            (role, line_spoken) = each_line.split(':', 2)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except ValueError:
            pass
    data.close()
else:
    print('missing')