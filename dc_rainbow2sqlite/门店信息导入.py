__author__ = 'joker_jiang'
#!/usr/bin/env python2
# -*-encoding:utf-8-*-

import sqlite3
with open(r'E:\learn_head_first_python\dc_rainbow2sqlite\门店档案.csv', 'r',encoding='UTF-8') as handle:
    # datas = [ln.split(',') for ln in handle]
    datas = [ln.strip('\n') for ln in handle]
print(datas)
# print(datas[1])
# cx = sqlite3.connect('D:/DC_RAINBOWCODE_test.db')
cx = sqlite3.connect('D:/DC_RAINBOWCODE.db')
cu = cx.cursor()
# insert_sql = 'insert into dc_rainbow_code (rainbow_code) values (%s)'
rainbow_code = []
store_code = []
name = []
for a in range(len(datas)):

    # print(a)i
    if a % 2 == 0:

        store_code.append(datas[a])
        # insert_sql = "insert into dcm_store (store_code) values ('%s')" % (datas[a])
        # cu.execute(insert_sql)
        # print(store_code)
    else:
        name.append(datas[a])
        # insert_sql = "insert into dcm_store (store_code, store_name) values ('%s')" % (store_code[i], name[i])
        # cu.execute(insert_sql)
        # print(name)
    # print(datas[a])
    # print(rainbow_code)
for i in range(len(store_code)):

    insert_sql = "insert into dcm_store (store_code, store_name) values ('%s','%s')" % (store_code[i], name[i])
    cu.execute(insert_sql)
    # cu.execute(insert_sql, str(rainbow_code))
    # cu.execute("insert into dc_rainbow_code (rainbow_code) values (?)", rainbow_code)
    # cu.execute('insert_sql = 'insert into dc_rainbow_code (rainbow_code) values (%s)',
    # cx.commit()
cx.commit()
cx.close()
print(store_code)
print(name)