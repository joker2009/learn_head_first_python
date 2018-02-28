__author__ = 'joker_jiang'
#!/usr/bin/env python2
# -*-encoding:utf-8-*-
# with open(r'E:\learn_head_first_python\dc_rainbow2sqlite\彩虹码数据包\6907376831150_20170803_露得清细白焕采密集修颜晚霜_50g_001.txt', 'r', encoding='UTF-8') as handle:
#     rainbow = [ln.strip(',') for ln in handle]
#     datas = [ln.strip('\n') for ln in handle]
# print(datas)
# print(rainbow)
# barcode = []
# rainbow_code = []
# other_code = []
#
#
# for a in range(len(datas)):
#     if a == 0:
#         barcode.append(datas[a])
#     else:
#         rainbow_code.append(datas[a].strip())
# print(barcode)
# print(rainbow_code)

all_line = []
rainbow_line = []
# barcode = []
# rainbow_code = []
for line in open(r'E:\learn_head_first_python\dc_rainbow2sqlite\彩虹码数据包\test.txt', 'r', encoding='UTF-8'):
    line = line.strip(' ')
    line = line.strip('\n')
    # print(line[0])
    # line = line.strip('')
    if str(line[:7]) == 'barcode':
        line = str(line[9:])
        all_line.append(line.strip(''))
    else:
        line = str(line[0:12])
        all_line.append(line.strip(''))


for i in range(len(all_line)):
    if len(all_line[i]) != 0:
        # print(all_line[i])
        rainbow_line.append(all_line[i])
print(rainbow_line)
# print(all_line[1:len(all_line)])

# print(len(all_line[0]))
# print(all_line)
# print(rainbow_line)
# for i in range(len(rainbow_line)):
#     if i == 0:
#         barcode.append(rainbow_line[i])
#     else:
#         rainbow_code.append(rainbow_line[i])
#
# print(barcode)
# print(rainbow_code)
#
# rainbow_line_new = []
# print(rainbow_line_new)
# barcode = barcode[]
# print(rainbow_line[:])
# rainbow_line_new = rainbow_line[1:]
# print(rainbow_line_new)

# file = open(r'E:\learn_head_first_python\dc_rainbow2sqlite\彩虹码数据包\text.txt', 'w')
# for i in range(len(rainbow_line_new)):
#
#     file.write(str(rainbow_line_new[i]))
# file.close()
# rainbow_line_new_new = []
# for lines in open(r'E:\learn_head_first_python\dc_rainbow2sqlite\彩虹码数据包\text.txt', 'r', encoding='UTF-8'):
#     lines = lines.strip(', ')
#     rainbow_line_new_new.append(lines.strip(', '))
# print(rainbow_line_new_new)