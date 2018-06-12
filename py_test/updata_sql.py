# -*- coding:UTF-8 -*-

"""
  批量替换sql语句,
  1、打开匹配文件，找到对应关系
  2、格式化替换update语句
  3、保存成本地文件
"""

# b = ['沃尔玛（嘉兴）配送中心', '132456']
# a = tuple(b)
#
sql = "update [Aveeno_SFTP].[dbo].[cus_match_log] set cus_name ='%s',upload_flag='0' where cus_id='%s' and cus_name like'%%?%%'"
# print(sql % a)


# 读取对应关系，再拼接SQL语句
def file_process():
    all_line = []
    with open(r"E:\aveeno\艾惟诺UPC上线20180604\经销商ID---经销商名称.csv", 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            # print(line)
            a = line.strip('\n').split(',')
            # print(type(a))
            # print(a)
            b = tuple(a)
            # print(sql % b)
            c = (sql % b)
            # print(c)
            d = str(c)
            all_line.append(d)
            # all_line.append(line.strip())
    return all_line


# 将收到的数据写入到创建的文件中
def write_file(list):
    with open('update_sql.sql', 'w+', encoding='UTF-8') as f:
        for i in list:
            # print(i)
            f.write(i + '\n')


if __name__ == '__main__':
    a = file_process()
    # print(a)
    write_file(a)
