__author__ = 'joker_jiang'

#!/usr/bin/env python2
# -*-encoding:utf-8-*-
import os
txt_path = r"E:\learn_head_first_python\dc_rainbow2sqlite\彩虹码数据包\已导入"
iterms = os.listdir(txt_path)
newlist = []
for names in iterms:
    if names.endswith('.txt'):
        newlist.append("E:/learn_head_first_python/dc_rainbow2sqlite/彩虹码数据包/已导入/" + names)
# newlist 是各文件的路径数组
print(newlist)

