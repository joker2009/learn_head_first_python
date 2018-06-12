__author__ = 'joker_jiang'
import csv


reader = csv.reader(open(r"C:\Users\joker_jiang\Desktop\新建文件夹\01.csv"), 'r', )
for unit in reader:
    print(unit[11])
    # print(unit)

def read_line_by_line(txt_path):

    all_line = []

    with open(txt_path, 'r') as f:
        for line in f.readlines():
            # print(line.strip())
            all_line.append(line.strip())
    return all_line
