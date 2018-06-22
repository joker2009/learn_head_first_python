__author__ = 'Administrator'
import pymysql

# 将当天生产的瓶码在MySQL数据库汇总进行激活。
# 将无法检索到的瓶码写入到“unKnow_bottle_code.txt”中
# 然后根据箱码搜索出不满箱的瓶码写入到“不满箱码.txt”中
# 输入的文件内格式为每行均只有一个瓶码

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
txt_path = r"E:\MTK\data processing\data_sourse\Oct\1019\line2\1019ALL_only_bottle.txt"
a = _Read_Line_by_Line(txt_path)
f = open("unKnow_bottle_code.txt", 'w', encoding="utf-8")
cursor =  connection.cursor()
for data in a:
    if len(data) == 14:
        bottle_code = data[:-1]
    else:
        bottle_code = data
    # 检索数据是否存在
#    print("检索数据是否存在")
    select__sql = "select * from bottle_box_relationship WHERE  bottle_code =  %s "
    a = cursor.execute(select__sql, bottle_code)
    result = cursor.fetchone()
    print(bottle_code + str(result))
    if a == 0:
        f.write(bottle_code)
        f.write('\n')

     # 检索是否曾经被使用过
    try:
        select__sql = "select taken from bottle_box_relationship WHERE bottle_code = %s "
        cursor.execute(select__sql, bottle_code)
        result = cursor.fetchone()
        taken = str(result).split(':')[1][:-1]
        if taken == 1:
            print(bottle_code+"曾经被使用")
            select_time = "select TakenTime from bottle_box_relationship WHERE bottle_code = %s"
            cursor.execute(select_time, bottle_code)
            result = cursor.fetchone()
    except:
        pass
    # 升级数据
 #   print("升级数据")
    update_sql = "UPDATE bottle_box_relationship SET taken = '1' WHERE bottle_code = %s "
    cursor.execute(update_sql,bottle_code)
    update_sql = "UPDATE bottle_box_relationship SET TakenTime = CURDATE() WHERE bottle_code = %s"
    cursor.execute(update_sql,str(bottle_code))
    # 检索箱码
   # print("检索箱码")
    select_sql = "select box_name from bottle_box_relationship WHERE bottle_code = %s"
    cursor.execute(select_sql,bottle_code)
    for each in cursor:
        result = str(each)
        box_number = result[14:-2]
        if box_number not in list:
            print(result)
            list.append(box_number)
f.close()
print("开始检索箱码")
path_arr_bottle = open("不满箱码.txt", 'w', encoding="utf-8")
arr = []
for number in list:
    print(number)
    select_sql = "select * from bottle_box_relationship WHERE box_name = %s AND taken = '0'"
    cursor.execute(select_sql,number)
    Last_box_name = ''
    for each in cursor:
        box_name = each['box_name']
        bottle_code = each['bottle_code']
        if box_name != Last_box_name:
            path_arr_bottle.write(box_name)
            path_arr_bottle.write('\n')
            path_arr_bottle.write("************" + bottle_code)
            path_arr_bottle.write('\n')
            Last_box_name = box_name
        else:
            path_arr_bottle.write("************" + bottle_code)
            path_arr_bottle.write('\n')
connection.commit()

path_arr_bottle.close()




