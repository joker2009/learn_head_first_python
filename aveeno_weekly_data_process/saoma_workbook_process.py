import openpyxl
import os
import csv

# 将收到的数据写入到创建的文件中
def write_file(list):
    with open('2018-7-05_t2.csv', 'a+', encoding='UTF-8') as f:

        for i in list:
            # print(i)
            f.write(i + '\n')
    print('文件写入成功，行数为')
    print(len(list))
    return len(list)

# 去掉None行和去重
def data_cleaning(data):
    all_data = []
    print(data)
    for i in data:
        # print(i[0:4])
        if i[0:4] != 'None' and   i[:3] != '无条码':
        # if i[:1] == "JB":
            all_data.append(i)
    return all_data

# 在文件目录下寻找EXCEL文件
def find_file_path(path):
    file_paths = os.listdir(path)
    excel_path_list = []
    for names in file_paths:
        if names.endswith('.xlsx'):
            # 添加需要导入的数据包地址，采用/，并在末尾加一个/
            excel_path_list.append(path + '/' + names)

    return excel_path_list

# 取开头为扫码账单的EXCEL表文件数据
def fetch_data(path):
    wb = openpyxl.load_workbook(path)
    ws = wb.worksheets[0]
    row_length = len(list(ws.rows))

    excel_data = []
    all_data = []
    for column in list(ws.columns)[7:]:
        # for cell in column:
        #     print(cell.value)
        # print(column[6:])
        excel_data.append(column[5:])
    for i in range(1,row_length-5):
        # print((excel_data[0][1].value)[:2])
        if str(excel_data[0][i].value)[:2] == "JB":
            all_data.append(str(excel_data[1][i].value) + ',' + str(excel_data[2][i].value) + ',' + str(excel_data[0][i].value))
    # print(all_data)
    return all_data




if  __name__ == '__main__':
    a = input('输入扫码账单EXCEL文件所造文件夹路径：')
    path_list = find_file_path(a)
    b = 0
    for i in range(len(path_list)):
        c = fetch_data(path_list[i])
        d = data_cleaning(c)
        e = write_file(d)
        b = e+b
    print("文件总行数：")
    print(b)
    # a = fetch_data(r"D:\My_doc\Aveeno数据\temple2\扫码账单 2018.6.11-6.18.xlsx")