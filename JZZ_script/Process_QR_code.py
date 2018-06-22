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
    return all_line

# 写入路径
txt_path = r"E:\MTK\data processing\data_sourse\Nov\1107\line2\-1\Log20161107.txt"
dir_path = txt_path[:-4]
out_put_log_path = dir_path + "_QR.log"
out_put_log = open(out_put_log_path, 'w', encoding="utf-8")
d = open(dir_path + "Data.log", 'w', encoding="utf-8")
a = _Read_Line_by_Line(txt_path)
Box_code_arr = []
rainbow_code_arr = []
Box_code = 0
Fail_number = 0
Add_code = 0
for data in a:
    if "瓶扫描失败" in data:
        Fail_number = Fail_number + 1
        #Box_code = Box_code + 1
    # if "【补扫】扫描成功，盒码：" in data:
    #     Box_code_arr.append(data)
    #     Add_code = Add_code + 1
    #     d.write(data)
    #     d.write('\n')
    if "瓶扫描成功" in data:
        Box_code = Box_code + 1
        # print(data)
        d.write(data)
        d.write('\n')
        Box_code_arr.append(data)
print("完成扫描的瓶数：" + str(Box_code))
print("失败的瓶数："+ str(Fail_number))
# print("成功补扫的瓶数："+ str(Add_code))

print(str( '%.2f'%(Fail_number/Box_code*100)) +"%")


for data in Box_code_arr:
    code_info = data.split("：")[1].split("--")
    if len(code_info) == 1:
        rainbow_code = code_info[0]
        if rainbow_code in rainbow_code_arr:
            continue
        rainbow_code_arr.append(rainbow_code)
    if len(code_info) == 2:
        rainbow_code = code_info[0]
        if rainbow_code in rainbow_code_arr:
            continue
        rainbow_code_arr.append(rainbow_code)
    if len(code_info) == 3:
        print(code_info)
        debug_info = code_info[2]
        rainbow_code = code_info[1]
        if rainbow_code in rainbow_code_arr:
            continue
        rainbow_code_arr.append(rainbow_code)
        # print(debug_info)
    time = data.split("------")[1][:-3]

for rainbow_code in rainbow_code_arr:
    out_put_log.write(rainbow_code)
    out_put_log.write('\n')
out_put_log.close()
d.close()
print("Create a file " + out_put_log_path)

