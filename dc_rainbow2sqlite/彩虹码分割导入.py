#!/usr/bin/env python2
# -*-encoding:utf-8-*-

import sqlite3

with open(r'E:\learn_head_first_python\dc_rainbow2sqlite\彩虹码数据包\未导入\690737683115020180117P001.txt', 'r', encoding='UTF-8') as handle:
    datas = [ln.strip('\n') for ln in handle]
print(datas)

barcode = []
rainbow_code = []
for i in range(len(datas)):
    if i == 0:
        barcode.append(datas[i])

    else:
        rainbow_code.append(datas[i])
print(barcode)
print(rainbow_code)
double_code = []
for i in range(len(rainbow_code)):
    double_code.append(barcode[0] + '*' + rainbow_code[i])
print(double_code)


# cx = sqlite3.connect('D:/DC_RAINBOWCODE_test.db')
cx = sqlite3.connect('D:/DC_RAINBOWCODE.db')
cu = cx.cursor()

for a in range(len(rainbow_code)):

    insert_sql = "insert into dc_rainbow_code (barcode, rainbow_code, double_code) values ('%s', '%s', '%s')" % (barcode[0], rainbow_code[a], double_code[a])
    cu.execute(insert_sql)
cx.commit()
cx.close()