__author__ = 'joker_jiang'

def sanitize(each_t):

    if '-' in each_t:
        splitter = '-'
    elif ':' in each_t:
        splitter = ':'
    else:
        return each_t
    (mins, secs) = each_t.split(splitter)
    return mins + '.' + secs

with open(r'E:\learn_head_first_python\chapter_5\hfpy_ch5_data\james.txt') as jaf:
    data = jaf.readline()
    james = data.strip().split(',')
    # print(james)

with open(r'E:\learn_head_first_python\chapter_5\hfpy_ch5_data\julie.txt') as juf:
    data = juf.readline()
    julie = data.strip().split(',')
    # print(julie)

with open(r'E:\learn_head_first_python\chapter_5\hfpy_ch5_data\mikey.txt') as mif:
    data = mif.readline()
    mikey = data.strip().split(',')
    # print(mikey)

with open(r'E:\learn_head_first_python\chapter_5\hfpy_ch5_data\sarah.txt') as saf:
    data = saf.readline()
    sarah = data.strip().split(',')
    # print(sarah)

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for each_t in james:
    clean_james.append(sanitize(each_t))
print(sorted(clean_james))

clean_julie = [sanitize(each_t) for each_t in julie]
print(clean_julie)