__author__ = 'Administrator'
import pymysql
def _Read_Line_by_Line(path):
    all_line = []
    for line in open(path, encoding="utf-8"):
        line = line.strip("\n")
        all_line.append(line)
        # print(all_line)

    return all_line
list = []
# 连接数据库
connection = pymysql.connect(host='localhost', user='root', password='',
                                 db='godenseed', charset='utf8', cursorclass = pymysql.cursors.DictCursor)

# 写入文件路径
txt_path = "E:\MTK\data processing\data_sourse\July/0722\第一批次ALL_only_bottle.txt"
cursor =  connection.cursor()
a = _Read_Line_by_Line(txt_path)
print("开始检索箱码")
path_arr_bottle = open("不满箱码4box_code.txt", 'w', encoding="utf-8")
for number in a:
    print(number)
    select_sql = "select * from bottle_box_relationship WHERE box_name = %s AND taken = '0'"
    cursor.execute(select_sql,number)
    for each in cursor:
        result = str(each)
        print(result)
        path_arr_bottle.write(result)
        path_arr_bottle.write('\n')
connection.commit()
path_arr_bottle.close()