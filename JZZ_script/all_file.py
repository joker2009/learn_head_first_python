#!/usr/bin/env python2
# -*-encoding:utf-8-*-

import os, sys
# 列出相关目录下所有的CSV文件
def all_file(dir):#定义一个寻找的函数
    import os #导入库
    file_path_arr = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path[-3:] == "csv":
                print(file_path)
                line = file_path[-5]
                file_path_arr.append([file_path, line])
    return (file_path_arr)

def read_csv(dir_arr):
    import csv
    index = {'6903800702393':'6903800702379','6903800701426':'6903800701402','6903800701419':'6903800701402','6903800702386':'6903800702379','6903800600071':'6903800600088','6903800703208':'6903800703192','6903800600439':'6903800600088'}
    for path in dir_arr:
        with open(path[0]) as csv_file:
            reader = csv.DictReader(csv_file)
            try:
                for row in reader:
                    print(row)
                    stook_code = row['二级数码']
                    product_time = row['对应时间']
                    line_number = str(path[1] + '号线')
                    batch_num = row['批次']
                    barcode = index[row['产品编码']]
                    rows = ' ,' + stook_code + ',' + product_time + ',' + line_number + ',' + barcode + ',' + batch_num
                    f.write(rows)
                    f.write('\n')
            except:
                pass

if __name__ == '__main__':
    dir = r"E:\MTK\data processing\data_sourse\Dec\1207line2"
    f = open(dir + ".csv", 'w', encoding="utf-8")
    title = "suitcase_code,stook_code,product_time,line_num	barcode(彩虹码对应的商品条码),batch_num	product_team,inspector,is_upload,"
    f.write(title)
    f.write('\n')
    dir_arr = all_file(dir)
    csv_dic_arr = read_csv(dir_arr)
    f.close()