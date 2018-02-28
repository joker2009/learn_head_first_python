#!/usr/bin/env python2
# -*-encoding:utf-8-*-

with open(r'E:\learn_head_first_python\dc_rainbow2sqlite\彩虹码数据包\已导入\露得清深层净化卸妆乳.txt', 'r', encoding='UTF-8') as handle:
    # datas = [ln.split(',') for ln in handle]
    # datas = [ln.strip('\n') for ln in handle]
    datas = [ln.strip('\n') for ln in handle]
print(datas)
# datas = []
# goods_code = []
# name = []
barcode = []
rainbow_code = []
for i in range(len(datas)):
    if i == 0:
        barcode.append(datas[i])

    else:
        rainbow_code.append(datas[i])
print(barcode)
print(rainbow_code)

# print(goods_code)
# print(name)
# print(datas[0])
# for a in range(len(datas)):
#     # print(a)
#     if a % 2 == 0:
#
#         store_code = datas[a]
#         print(store_code)
#     else:
#         name = datas[a]
#         print(name)

# print(store_code)
# print(name)
# print(datas[1])