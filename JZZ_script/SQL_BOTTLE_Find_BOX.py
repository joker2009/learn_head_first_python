__author__ = 'Administrator'
import pymysql
# 根据瓶码来寻找箱码的脚本
#　将瓶码写入到一个文件中，文件的格式为每行一个瓶码
# 输入文件路径
# 输出一个文件，内容为包含这些瓶码的箱码
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
                                 db='godenseed', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

# 写入路径
txt_path = r"E:\MTK\data processing\第六批次ALL_only_bottle.txt"
a = _Read_Line_by_Line(txt_path)
cursor =  connection.cursor()
for data in a:
    bottle_code = data
    select_sql = "select box_name from bottle_box_relationship WHERE bottle_code = %s"
    cursor.execute(select_sql,bottle_code)
    for each in cursor:
        result = str(each)
        box_number = result[14:-2]
        if box_number not in list:
            print(result)
            list.append(box_number)

print("开始生成箱码")
Create_path = txt_path[:-4] + "_box_code.txt"
print(Create_path)
path_arr_bottle = open(Create_path, 'w', encoding="utf-8")
for number in list:
    path_arr_bottle.write(number)
    path_arr_bottle.write('\n')
path_arr_bottle.close()

#
# if __name__ == '__main__':
#     bottle_code = "10b630011644"
