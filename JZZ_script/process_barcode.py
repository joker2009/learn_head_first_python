__author__ = 'Administrator'


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

# 创建文件夹，以保存数组中的数值。
# 参数包括
# path：保存路径（包含保存的格式）
# arr：需要保存的数组
# save_mode：文件的写入方式，默认为W覆盖式可写
# r只读，w可写，a追加
def create_txt(path, arr, save_mode="w"):
    f = open(path, save_mode, encoding="utf-8")  # r只读，w可写，a追加
    for data in arr:
        f.write(data + '\n')
    f.close()


# 写入路径
txt_path = r"E:\MTK\data processing\data_sourse\F\0124line2\-4\Log20170124.txt"
dir_path = txt_path[:-4]

d = open(dir_path + "瓶失败数据.log", 'w', encoding="utf-8")
e = open(dir_path + "盒失败数据.log", 'w', encoding="utf-8")
f = open(dir_path + "瓶扫描数据.log", 'w', encoding="utf-8")
g = open(dir_path + "盒扫描数据.log", 'w', encoding="utf-8")
h = open(dir_path + "数据汇总.log", 'w', encoding="utf-8")
a = _Read_Line_by_Line(txt_path)

bottle_code_arr = []
bottle_fail_arr = []

box_code_arr = []
box_fail_arr = []
Add_box_code_arr = []

box_number = 0


for data in a:
    if "瓶扫描失败" in data:
        bottle_fail_arr.append(data)
        d.write(data)
        d.write('\n')
        h.write(data)
        h.write('\n')
    if "瓶扫描成功" in data:
        bottle_code_arr.append(data)
        f.write(data)
        f.write('\n')
        h.write(data)
        h.write('\n')
    if "盒扫描失败" in data:
        box_fail_arr.append(data)
        box_number = box_number + 1
        e.write(data)
        e.write('\n')
        h.write(data)
        h.write('\n')
    if "【补扫】扫描成功，盒码：" in data:
        box_code_arr.append(data)
        Add_box_code_arr.append(data)
        g.write(data)
        g.write('\n')
        h.write(data)
        h.write('\n')
    if "盒扫描成功" in data:
        box_code_arr.append(data)
        box_number = box_number + 1
        g.write(data)
        g.write('\n')
        h.write(data)
        h.write('\n')

print("完成扫描的瓶数：" + str(len(bottle_code_arr)))
print("失败的瓶数："+ str(len(bottle_fail_arr)))
print("瓶失败率："+ str( '%.2f'%(len(bottle_fail_arr)/len(bottle_code_arr)*100)) +"%")

print("完成扫描的盒数number：" + str(box_number))
print("完成扫描的盒数：" + str(len(box_code_arr)))
print("失败的盒数："+ str(len(box_fail_arr)))
print("成功补扫的盒数："+ str(len(Add_box_code_arr)))
print("盒失败率："+ str( '%.2f'%(len(box_fail_arr)/len(box_code_arr)*100)) +"%")

log = []
log.append("完成扫描的瓶数：" + str(len(bottle_code_arr)))
log.append("失败的瓶数："+ str(len(bottle_fail_arr)))
log.append("瓶失败率："+ str( '%.2f'%(len(bottle_fail_arr)/len(bottle_code_arr)*100)) +"%")

log.append("完成扫描的盒number：" + str(box_number))
log.append("完成扫描的盒数：" + str(len(box_code_arr)))
log.append("失败的盒数："+ str(len(box_fail_arr)))
log.append("成功补扫的盒数："+ str(len(Add_box_code_arr)))
log.append("盒失败率："+ str( '%.2f'%(len(box_fail_arr)/len(box_code_arr)*100)) +"%")

log_path = txt_path[:-4] + "处理报告.txt"
create_txt(log_path, log)

# box = []
# box_path = txt_path[:-4] + "盒码数据.txt"
# create_txt(box_path, box_code_arr,"a")
#
# bottle = []
# bottle_path = txt_path[:-4] + "瓶码数据.txt"
# create_txt(bottle_path, bottle_code_arr,"a")
