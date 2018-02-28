__author__ = 'joker_jiang'
#!/usr/bin/env python2
# -*-encoding:utf-8-*-

import sqlite3
with open(r'E:\learn_head_first_python\dc_rainbow2sqlite\露得清深层柔珠洗面乳.txt', 'r') as handle:
    datas = [ln.replace(',', '').strip('\n') for ln in handle]
print(datas)
# print(datas[1])
cx = sqlite3.connect('D:/DC_RAINBOWCODE_test.db')
cu = cx.cursor()
# insert_sql = 'insert into dc_rainbow_code (rainbow_code) values (%s)'
rainbow_code = []
for a in range(0, 1000000):
    # print(a)
    rainbow_code = datas[a]
    # print(datas[a])
    print(rainbow_code)
    insert_sql = "insert into dc_rainbow_code (rainbow_code) values ('%s')" % (rainbow_code)
    cu.execute(insert_sql)
    # cu.execute(insert_sql, str(rainbow_code))
    # cu.execute("insert into dc_rainbow_code (rainbow_code) values (?)", rainbow_code)
    # cu.execute('insert_sql = 'insert into dc_rainbow_code (rainbow_code) values (%s)',
    cx.commit()
cx.close()