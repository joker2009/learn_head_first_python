#!/usr/bin/env python2
# -*-encoding:utf-8-*-
# rainbow_code = []
# f = open(r'E:\learn_head_first_python\dc_rainbow2sqlite\露得清深层柔珠洗面乳.txt', 'r')
# s = f.read()
# rainbow_code = s
# print(rainbow_code[0])

path = r'E:\learn_head_first_python\dc_rainbow2sqlite\露得清深层柔珠洗面乳.txt'
def _Read_Line_by_Line(path):
    all_line = []
    for line in open(path, encoding="utf-8"):
        line = line.strip("\n")
        all_line.append(line)
    return all_line

all_line = _Read_Line_by_Line(path)
all_line
print(all_line)

