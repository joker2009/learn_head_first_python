import pymysql

def _Read_Line_by_Line(path):
    all_line = []
    for line in open(path, encoding="utf-8"):
        line = line.strip("\n")
        all_line.append(line)
        # print(all_line)

    return all_line
# 连接数据库
connection = pymysql.connect(host='localhost', user='root', password='',
                                 db='godenseed', charset='utf8', cursorclass = pymysql.cursors.DictCursor)
cursor =  connection.cursor()
txt_path = "E:\MTK\data processing/box_code.txt"
a = _Read_Line_by_Line(txt_path)
for data in a:
    bottle_code = data
    # 检索是否曾经被使用过
    select__sql = "select COUNT(*) from bottle_box_relationship WHERE box_name = %s "
    cursor.execute(select__sql, bottle_code)
    result = cursor.fetchone()
    print(bottle_code + str(result))