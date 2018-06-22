__author__ = 'Administrator'
import xlrd
import pymysql
# 单独升级瓶码的发码日记的脚本，已经集成到search_bottle.py中

# 打开EXCEL文件
excel = xlrd.open_workbook('E:\MTK\data processing\data_sourse\data_bage/20160607码数据.xlsx')
# 设置发包时间
Creat_time = "2016-06-07"
# 连接数据库
connection = pymysql.connect(host='localhost', user='root', password='',
                             db='godenseed', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
#获取第一个sheet
sheet = excel.sheets()[0]
cursor = connection.cursor()
try:
    for a in range(0, 1000000000):
        issue = sheet.row_values(a)
        bottle_code = issue[0]
        box_name = issue[1]
        print("准备插入瓶码："+bottle_code)
        print("此瓶码所属的箱码："+ box_name)
        # print(a + 1)
        try:
            update_sql = "UPDATE bottle_box_relationship SET box_product_time = "+Creat_time+" WHERE bottle_code = %s"
            cursor.execute(update_sql,str(bottle_code))
            print(bottle_code + "瓶码时间升级成功")
        except:
            print("升级时间失败")
            pass
except:
    pass
connection.commit()
print(a)

