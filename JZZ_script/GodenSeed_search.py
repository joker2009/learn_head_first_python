__author__ = 'bear_fu'
import os
import datetime

# 逐行读取文档内容
def _Read_Line_by_Line(path):
    all_line = []
    for line in open(path, encoding="utf-8"):
        line = line.strip("\n")
        all_line.append(line)
    # print(all_line)

    return all_line


# 检索输入路径下所有包含“检索条件”的路径
# 默认的检索条件是"批次ALL.txt"
# 返回一个包含所有符合条件路径的数组
def seach_path(dir=r"F:\Oct\1006", filt="Log.txt"):
    arr = []
    ARR_ALL = []

    for root, dirs, files in os.walk(dir):
        for file in files:
            # print(os.path.join(root, file))
            arr.append(os.path.join(root, file))

    for a in arr:
        if filt in a:
            ARR_ALL.append(a)

    return ARR_ALL


# 创建文件夹，以保存数组中的数值。
# 参数包括
# path：保存路径（包含保存的格式）
# arr：需要保存的数组
# save_mode：文件的写入方式，默认为W覆盖式可写
# r只读，w可写，a追加
def create_txt(path, arr, save_mode="w"):
    f = open(path, save_mode, encoding="utf-8")  # r只读，w可写，a追加
    for a in arr:
        f.write(a + '\n')
    f.close()


# 对目标路径下的文件进行处理
# 分别存储瓶扫描失败，盒扫描失败，盒成功补扫的时间信息
# 保存的文件会放置在原始文件路径下
# 输入为包含需要处理的文件的路径的数组
def start(path_arr=["E:\MTK\data processing\data_sourse\Oct\1013\第一批次ALL.txt"]):
    # try:
    #     os.remove(r"F:\untitled\save.log")
    # except:
    #     print("目录文件不存在")
    for path in path_arr:
        save_arr = []
        bottle_arr = []
        box_arr = []
        add_arr = []
        log = []
        txt_arr = _Read_Line_by_Line(path)
        long = len(txt_arr)
        for a in range(0, long):
            if "成功" not in txt_arr[a]:
                del txt_arr[a]
            else:
                break
        for a in txt_arr:
            if "瓶扫描失败" in a:
                bottle_arr.append(a)
            elif "盒扫描失败" in a:
                box_arr.append(a)
            elif "【补扫】存入本地对应关系表" in a:
                add_arr.append(a)

        log.append("瓶扫描失败数量为： " + str(len(bottle_arr)))
        log.append("盒扫描失败数量为： " + str(len(box_arr)))
        log.append("成功补扫的数量为： " + str(len(add_arr)))

        log_path = path[:-4] + "错误报告.txt"
        box_path = path[:-4] + "盒失败时间信息.txt"
        add_path = path[:-4] + "成功补扫时间信息.txt"
        bottle_path = path[:-4] + "瓶失败时间信息.txt"
        create_txt(box_path, box_arr)
        save_arr.append(box_path)
        create_txt(add_path, add_arr)
        save_arr.append(add_path)
        create_txt(bottle_path, bottle_arr)
        save_arr.append(bottle_path)
        # create_txt(r"F:\untitled\save.log", save_arr, "a")
        create_txt(log_path, log)

# 这个没用到，暂时不管
def err():
    path = r"F:\untitled\save.log"
    arr = _Read_Line_by_Line(path)
    print(arr)
    list = []
    err = []
    for a in arr:
        arr = _Read_Line_by_Line(a)
        date_arr = []
        three_min = datetime.timedelta(minutes=3)

        for a in arr:
            date_time = datetime.datetime.strptime(a[6:25], '%Y-%m-%d %H:%M:%S')
            date_arr.append(date_time)

        for a in range(0, len(date_arr) - 1):
            if date_arr[a + 1] - date_arr[a] < three_min:
                print(date_arr[a + 1])
                print(date_arr[a])
                print(date_arr[a + 1] - date_arr[a])
                if date_arr[a] not in err:
                    err.append(date_arr[a])
                if date_arr[a + 1] not in err:
                    err.append(date_arr[a + 1])

    print(len(err))


def lan(dir):
    path_arr = seach_path(dir)
    for a in path_arr:
        print(a)
    print("正在生成相关文档，请稍候")
    start(path_arr)


if __name__ == '__main__':
    print("Start")
    dir = input("请输入需要处理的文件夹绝对路径: ")
    lan(dir)







