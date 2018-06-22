__author__ = 'Administrator'
def _Read_Line_by_Line(path):
    all_line = []
    for line in open(path, encoding="utf-8"):
        line = line.strip("\n")
        all_line.append(line)
        # print(all_line)

    return all_line
import pymysql
# 输入箱码，搜索箱码的发码日期
# 将需要搜索的箱码写到文件中，格式为每行一个箱码
list = []


# 连接数据库
connection = pymysql.connect(host='localhost', user='root', password='',
                                 db='godenseed', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

# 写入路径
txt_path = "E:\MTK\data processing\data_sourse\June/0628/box_code.txt"
a = _Read_Line_by_Line(txt_path)
cursor = connection.cursor()
for data in a:
    box_name = data
    select_sql = "select box_product_time from bottle_box_relationship WHERE box_name = %s"
    cursor.execute(select_sql,box_name)
    for each in cursor:
        result = str(each)
        if result not in list:
            print(result)
            list.append(result)

print("开始生成日期")
path_arr_bottle = open("day.txt", 'w', encoding="utf-8")
for number in list:
    path_arr_bottle.write(number)
    path_arr_bottle.write('\n')
path_arr_bottle.close()

