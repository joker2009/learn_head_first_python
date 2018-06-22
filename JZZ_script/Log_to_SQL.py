_author__ = 'Administrator'
import re
def _Read_Line_by_Line(path):
    all_line = []
    for line in open(path, encoding="utf-8"):
        line = line.strip("\n")
        all_line.append(line)
        # print(all_line)

    return all_line
# 写入原始的文件路径
# 要求是完整的批次
txt_path = r"E:\MTK\data processing\data_sourse\Dec\1206line2\1bu.txt"
all_line = _Read_Line_by_Line(txt_path)

# 配置生成的批次号
Batch = "2016120612三河商超"

# 配置生成的产品Batch编码
PrdCode = "6903800600439"

# 配置输出的名称
name = txt_path[:-3] +"sql"
print(name)
out_put_log = open(name, 'w', encoding="utf-8")

# 完整的输出样例
# Insert Into CodeList (Code1,Batch,PrdCode,PrdDateTime) VALUES ('1015q0072851','2016060712LJJLYJD','6903800702379','2016/6/7 7:40');

for line in all_line:
    log_time = line[6:25]
    information = line[39:]
    try:
        if information[:5] == "瓶扫描成功":
            code_re = re.compile(r'，(.*)')
            code = re.findall(code_re,information)
            Code1 = code[0][3:]
            PrdDateTime = log_time
            # print(log_time ,bottle_number)
            out_put = "Insert Into CodeList (Code1,Batch,PrdCode,PrdDateTime) VALUES('"+Code1+"','"+Batch+"','"+PrdCode+"','"+PrdDateTime+"');"
            out_put_log.write(out_put)
            out_put_log.write('\n')
            print(out_put)
    except:
        pass

