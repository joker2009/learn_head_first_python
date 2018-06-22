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
txt_path = r"E:\MTK\data processing\data_sourse\Nov\1108\line2\-4\Log20161108.txt"
dir_path = txt_path[:-4]
out_put_log_path = dir_path + "_QR.log"
out_put_log_path = dir_path + "_RainBow.log"
out_put_log = open(out_put_log_path, 'w', encoding="utf-8")
d = open(dir_path + "Data.log", 'w', encoding="utf-8")
a = _Read_Line_by_Line(txt_path)

bottle_code_arr = []
rainbow_code_arr = []
bottle_code = 0
bottle_Fail_number = 0
Add_bottle_code = 0

Box_code_arr = []
Box_code = 0
Box_Fail_number = 0
Box_Add_code = 0
Box_Add_arr = []
add_arr = []

def create_txt(path, arr, save_mode="w"):
    f = open(path, save_mode, encoding="utf-8")  # r只读，w可写，a追加
    for a in arr:
        f.write(a + '\n')
    f.close()

for data in a:
    if "瓶扫描失败" in data:
        bottle_Fail_number = bottle_Fail_number + 1
        #bottle_code = bottle_code + 1
    if "瓶扫描成功" in data:
        bottle_code = bottle_code + 1
        # print(data)
        d.write(data)
        d.write('\n')
        bottle_code_arr.append(data)
    if "盒扫描失败" in data:
        Box_Fail_number = Box_Fail_number + 1
        Box_code = Box_code + 1
    if "【补扫】扫描成功，盒码：" in data:
        Box_code_arr.append(data)
        Box_Add_code = Box_Add_code + 1
        Box_Add_arr.append(data)
        d.write(data)
        d.write('\n')
    if "盒扫描成功" in data:
        Box_code = Box_code + 1
        # print(data)
        Box_code_arr.append(data)
        d.write(data)
        d.write('\n')


        log = []
        log.append("完成扫描的瓶数：" + str(bottle_code))
        log.append("失败的瓶数："+ str(bottle_Fail_number))
        log.append("瓶失败率："+ str( '%.2f'%(bottle_Fail_number/bottle_code*100)) +"%")

        log.append("完成扫描的盒数：" + str(Box_code))
        log.append("失败的盒数："+ str(Box_Fail_number))
        log.append("成功补扫的盒数："+ str(Box_Add_code))
        log.append("盒失败率："+ str( '%.2f'%(Box_Fail_number/Box_code*100)) +"%")

        log_path = txt_path[:-4] + "处理报告.txt"
        create_txt(log_path, log)

        box = []
        box.append("完成扫描的盒码：" + str(Box_code_arr))
        box.append("成功补扫的盒码：" + str(Box_Add_arr))
        box_path = txt_path[:-4] + "盒码处理报告.txt"
        create_txt(box_path, box)

print("完成扫描的瓶数：" + str(bottle_code))
print("失败的瓶数："+ str(bottle_Fail_number))
print("瓶失败率："+ str( '%.2f'%(bottle_Fail_number/bottle_code*100)) +"%")

print("完成扫描的盒数：" + str(Box_code))
print("失败的盒数："+ str(Box_Fail_number))
print("成功补扫的盒数："+ str(Box_Add_code))
print("盒失败率："+ str( '%.2f'%(Box_Fail_number/Box_code*100)) +"%")

for data in bottle_code_arr:
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

