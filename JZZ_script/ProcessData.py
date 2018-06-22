import re
__author__ = 'Administrator'
arr = []

# 逐行读取文件并将其作为数组返回
# Input 文件路径以及文件名称
# Output 包含文件内容的数组，可能出现空
def _Read_Line_by_Line(path):
    all_line = []
    for line in open(path, encoding="utf-8"):
        line = line.strip("\n")
        all_line.append(line)
        # print(all_line)

    return all_line
def Process_data(txt_path):

    dir_path= txt_path[:-4]
    a = _Read_Line_by_Line(txt_path)

    box_ture = "盒扫描成功"
    bottle_ture = "瓶扫描成功"
    arr_box = []
    arr_bottle = []
    arr_add = []
    for data in a:
        all_information = data
        information = data[39:]
        if information == "彩虹枪返回‘decode failed’，盒扫描失败，剔除":
            box_number = "error"
            arr_box.append(all_information)
        if information[:5] == "盒补扫扫描":
            box_number = all_information
            arr_add.append(box_number)
        if information[:5] == "盒扫描成功":
            box_number = all_information
            arr_box.append(box_number)
        if information[:5] == "瓶扫描成功":
            bottle_number = all_information
            if bottle_number in arr_bottle:
                continue
            arr_bottle.append(bottle_number)

    # print(arr_bottle)
    # print(arr_add)
    # print(arr_box)

    path_arr_bottle =dir_path+ "_arr_bottle.txt"
    path_arr_bottle = open(path_arr_bottle, 'w', encoding="utf-8")
    for arr in arr_bottle:
        #print(arr)
        path_arr_bottle.write(arr)
        path_arr_bottle.write('\n')
    path_arr_bottle.close()

    path_arr_bottle =dir_path+ "_only_bottle.txt"
    path_arr_bottle = open(path_arr_bottle, 'w', encoding="utf-8")
    for arr in arr_bottle:
        code_re = re.compile(r'：(.*)')
        code = re.findall(code_re,arr)
        print(code[0])
        path_arr_bottle.write(code[0].strip())
        path_arr_bottle.write('\n')
    path_arr_bottle.close()
    print(len(arr_bottle))
if __name__ == '__main__':
    txt_path = r'E:\MTK\data processing\data_sourse\0308\0314line2\-1\第一批次.txt'
    Process_data(txt_path)
    # path_arr_add = dir_path+ "_arr_add.txt"
    # path_arr_add_file = open(path_arr_add, 'w', encoding="utf-8")
    # for arr in arr_add:
    #     path_arr_add_file.write(arr)
    #     path_arr_add_file.write('\n')
    # path_arr_add_file.close()
    #
    # path_arr_box = dir_path+ "_arr_box.txt"
    # path_arr_box_file = open(path_arr_box, 'w', encoding="utf-8")
    # for arr in arr_box:
    #     path_arr_box_file.write(arr)
    #     path_arr_box_file.write('\n')
    # path_arr_box_file.close()


    # path_arr_box = dir_path+ "_all_box.log"
    # path_arr_box_file = open(path_arr_box, 'w', encoding="utf-8")
    # number = 0
    # for arr in arr_box:
    #     # print(arr[39:])
    #     if arr[39:] !="彩虹枪返回‘decode failed’，盒扫描失败，剔除":
    #         # print(arr)
    #         time_re = re.compile(r'------(.*?)------')
    #         time = re.findall(time_re,arr)
    #         code = arr[-12:]
    #         # if time !=[] :
    #         _time =  time[0].replace('-','/')[:-7]
    #         information_ = _time + "," + str(code)
    #         print(information_)
    #         path_arr_box_file.write(information_)
    #         path_arr_box_file.write('\n')
    #     else:
    #         # "盒扫描成功，盒码：247271177384"
    #         # "盒补扫扫描成功，盒码：265714807315"
    #         add = arr_add[number]
    #         time_re = re.compile(r'------(.*?)------')
    #         time = re.findall(time_re,arr)
    #         _time =  time[0].replace('-','/')[:-7]
    #         add_data = _time +"," + add[-12:]
    #         #print(add_data)
    #         path_arr_box_file.write(add_data)
    #         path_arr_box_file.write('\n')
    #         number =number + 1

    # path_arr_box_file.close()




