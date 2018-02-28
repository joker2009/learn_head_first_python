__author__ = 'joker_jiang'
__author__ = 'joker_jiang'
#!/usr/bin/env python2
# -*-encoding:utf-8-*-
import sqlite3
# cx = sqlite3.connect('D:/DC_RAINBOWCODE_test.db')
cx = sqlite3.connect('D:/DC_RAINBOWCODE.db')
cu = cx.cursor()
with open(r'E:\learn_head_first_python\dc_rainbow2sqlite\商品档案.csv', 'r', encoding='UTF-8') as handle:
    # datas = [ln.split(',') for ln in handle]
    datas = [ln.strip('\n') for ln in handle]
print(datas)

goods_code = []
name = []
for i in range(len(datas)):
    if i % 2 == 0:
        name.append(datas[i])

    else:
        goods_code.append(datas[i])


for i in range(len(goods_code)):

    insert_sql = "insert into dcm_goods (barcode, goods_name) values ('%s','%s')" % (goods_code[i], name[i])
    cu.execute(insert_sql)
    # cu.execute(insert_sql, str(rainbow_code))
    # cu.execute("insert into dc_rainbow_code (rainbow_code) values (?)", rainbow_code)
    # cu.execute('insert_sql = 'insert into dc_rainbow_code (rainbow_code) values (%s)',
    # cx.commit()
cx.commit()
cx.close()
print(goods_code)
print(name)