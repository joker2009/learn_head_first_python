__author__ = 'joker_jiang'

# shit_code
import os
import sqlite3
cx = sqlite3.connect('D:/DC_RAINBOWCODE_test.db')
cu = cx.cursor()
# 添加需要导入的数据包地址
txt_path = r"E:\learn_head_first_python\dc_rainbow2sqlite\彩虹码数据包\test"
iterms = os.listdir(txt_path)
newlist = []
for names in iterms:
    if names.endswith('.txt'):
        # 添加需要导入的数据包地址，采用/，并在末尾加一个/
        newlist.append("E:/learn_head_first_python/dc_rainbow2sqlite/彩虹码数据包/test/" + names)
#newlist是各文件的路径数组
print(newlist)

all_line = []
rainbow_line = []
double_code = []
barcode = []
rainbow_code = []
for i in range(len(newlist)):

    list_path = newlist[i]
    # print(list_path)
    for line in open(list_path, 'r', encoding='UTF-8'):
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
    for a in range(len(all_line)):
        if len(all_line[a]) != 0:
            # print(all_line[i])
            rainbow_line.append(all_line[a])
    del all_line[:]

    print(rainbow_line)
    print(len(rainbow_line))
    del barcode[:]
    for d in range(len(rainbow_line)):
        if d == 0:
            barcode.append(rainbow_line[d])

        else:
            rainbow_code.append(rainbow_line[d])
    print(barcode)
    for b in range(len(rainbow_code)):
        double_code.append(barcode[0] + '*' + rainbow_code[b])
    print(rainbow_code)
    print(double_code)
    for c in range(len(rainbow_code)):

        insert_sql = "insert into dc_rainbow_code (barcode, rainbow_code, double_code) values ('%s', '%s', '%s')" % (barcode[0], rainbow_code[c], double_code[c])
        cu.execute(insert_sql)
    cx.commit()
    del double_code[:]
    del rainbow_line[:]
    del barcode[:]
    del rainbow_code[:]

# del rainbow_code[:]
cx.close()
# print(rainbow_line)
# print(len(rainbow_line))
# del rainbow_line[:]
# print(rainbow_line)
# print(len(rainbow_line))