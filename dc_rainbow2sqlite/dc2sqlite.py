__author__ = 'joker_jiang'
import sqlite3
with open(r'E:\learn_head_first_python\dc_rainbow2sqlite\露得清深层柔珠洗面乳.txt', 'r') as handle:
    datas = [ln.replace(',', '').strip('\n') for ln in handle]
print(datas)
print(datas[1])
cx = sqlite3.connect('D:/DC_RAINBOWCODE.db')
# rainbow_code = []
# rainbow_code[0] =
# print(rainbow_code[0])
cu = cx.cursor()
# for a in
# # sql = 'insert into dc_rainbow_code (rainbow_code) values ("6907376830122*225277181866")'
#
insert_sql = "insert into dc_rainbow_code (rainbow_code) values ("'+datas+'")"
cu.execute(insert_sql)
# cu.execute(insert_sql)

cx.commit()
cx.close()