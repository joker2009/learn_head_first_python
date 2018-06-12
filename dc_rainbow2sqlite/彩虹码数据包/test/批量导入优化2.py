__author__ = 'joker_jiang'
import os
import sqlite3


class RainbowSql(object):
    def __init__(self, txt_path):
        self.txt_path = txt_path

    def find_txt_path(self, txt_path):
        file_paths = os.listdir(txt_path)
        path_list = []
        for names in file_paths:
            if names.endswith('.txt'):
                # 添加需要导入的数据包地址，采用/，并在末尾加一个/
                path_list.append(txt_path + '/' + names)
        # print(path_list)
        return path_list


# 逐行读取，并去掉末尾换行符
    def read_line_by_line(self, txt_path):

        all_line = []

        with open(txt_path, 'r') as f:
            for line in f.readlines():
                # print(line.strip())
                all_line.append(line.strip())
        return all_line


# 去掉空行
    def remove_white_block(self, list_lines):
        new_lines = []
        for a in range(len(list_lines)):
            if len(list_lines[a]) != 0:
                new_lines.append(list_lines[a])
        return new_lines


# 取barcode和rainbow_code数据,并分离数据,合成barcode_rainbow

    def fetch_code(self, lines_list):
        barcode_list = []
        rainbow_list = []
        barcode_rainbow = []
        for line in lines_list:
            if str(line[:7]) == 'barcode':
                line = str(line[9:])
                barcode_list.append(line)
            else:
                line = str(line[:12])
                rainbow_list.append(line)
        for num in range(len(rainbow_list)):
            barcode_rainbow.append(barcode_list[0] + '*' + rainbow_list[num])
        return barcode_list, rainbow_list, barcode_rainbow


# 插入数据库
    def rainbow_sql(self, barcode, rainbow_code, barcode_rainbow, db_path='D:/DC_RAINBOWCODE_test.db'):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        try:
            for num in range(len(rainbow_code)):
                insert_sql = "insert into dc_rainbow_code (barcode, rainbow_code, barcode_rainbow) values ('%s', '%s', '%s')" \
                             % (barcode[0], rainbow_code[num], barcode_rainbow[num])
                cur.execute(insert_sql)
            conn.commit()
        except Exception as e:
            print('插入失败')
            print('失败原因:', e)
        else:
            print('数据插入成功')


if __name__ == '__main__':
    c = 'E:/learn_head_first_python/dc_rainbow2sqlite/彩虹码数据包/test'
    a = RainbowSql(c)
    b = a.find_txt_path(c)
    print(b)