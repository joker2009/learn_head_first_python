__author__ = 'Administrator'
import pymysql


def _Read_Line_by_Line(path):
    all_line = []
    for line in open(path, encoding="utf-8"):
        line = line.strip("\n")
        all_line.append(line)
        # print(all_line)

    return all_line


connection = pymysql.connect(host='localhost', user='root', password='',
                             db='godenseed', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()
txt_path = "E:\MTK\data processing\第四批次ALL_only_bottle.txt"

a = _Read_Line_by_Line(txt_path)
f = open("D_code.txt", 'w', encoding="utf-8")

cursor = connection.cursor()
for data in a:
    bottle_code = '"'+data + '"'
    if len(data) == 14:
        bottle_code =  '"'+ data[:-1] + '"'
    try:
        insert_sql = "select * from bottle_box_relationship_backup where bottle_code = " + bottle_code
        a = cursor.execute(insert_sql)
        if a == 1:
            print(bottle_code)
    except:
        print("数据插入失败"+ str(bottle_code))
        f.write(bottle_code)
        f.write("/n")
        pass
f.close()