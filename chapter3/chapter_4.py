__author__ = 'joker_jiang'
import os
from nester import print_lol
man = []
other = []
try:
    os.chdir('E:\learn_head_first_python\chapter3')
    file_path2 = os.getcwd()
    data = open('sketch.txt')
    for each_line in data:
        try:

            (role, line_spoken) = each_line.split(':', 2)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                # line_spoken = line_spoken.strip()
                man.append(line_spoken)
            elif role == 'Other Man':
                # line_spoken = line_spoken.strip()
                other.append(line_spoken)
            # print(role, end='')
            # print(' said: ', end='')
            # print(line_spoken, end='')

        except ValueError:
            pass
    data.close()
except IOError:
    print('missing')


# print(man)
# print(other)

try:
    man_file = open('man_data.txt', 'w')
    other_file = open('other_data.txt', 'w')

    print_lol(man, file=man_file,)
    print_lol(other, file=other_file)
    man_file.close()
    other_file.close()
except IOError:
    print('missing')
# finally:
#     man_file.close()
#     other_file.close()

try:
    with open('man_data.txt', 'w') as data:
        print(man, file=man_file)
except IOError as err:
    print('missing' + str(err))
