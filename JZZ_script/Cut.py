import re

# 按照规则切分相应的批次，由于可能出现同批次重启的原因也许要人工重新合并
def Cut_file():
    file_path = r"E:\MTK\data processing\data_sourse\0308\0314line2\-4\Log20170314.txt"
    f = open(file_path, "r", encoding="utf-8")
    lines = f.readlines()
    a = -1
    arr_box = []
    for data in range(0, len(lines)):
        all_information = lines[data]
        information = str(all_information[-13:-1])
        if information == "补扫扫描枪串口打开成功！":
            arr_box.append([data])
            a = a + 1
        try:
            all_information = all_information.strip("\n")
            arr_box[a].append(all_information)
        except:
            pass
    arr_number = ['一','二','三','四','五','六','七','八','九','十','十一','十二','十三','十四','十五','十六','十七','十七','十八','十九','二十','二十一','二十二','二十三','二十四','二十五','二十六','二十七','二十八','二十九','三十']
    for a in range(0, len(arr_box)):
        print(arr_box[a][2:])
        path =file_path[:-15] + "第"+arr_number[a]+"批次"+".txt"
        print(path)
        file = open(path, 'w', encoding="utf-8")
        for box in arr_box[a][2:]:
            file.write(box)
            file.write('\n')
        file.close()

# 提取出一天生产的所有瓶码。按照“瓶码，时间的格式进行排列”

if __name__ == '__main__':
    # file_path = "E:\MTK\data processing\data_sourse\0615\0615-1\Log20160615.txt"
    # save_path = "E:\MTK\data processing\data_sourse\0615\0615-1"
    # code_re = re.compile(r'(.*)L')
    # code = re.findall(code_re, file_path)
    # print(code)
    Cut_file()