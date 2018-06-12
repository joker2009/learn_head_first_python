__author__ = 'joker_jiang'

#Delete blanklines of infile
def del_blank_line(infile, outfile):

    infp = open(infile, "r")
    outfp = open(outfile, "w")
    lines = infp.readlines()
    for li in lines:
        if li.split():
            outfp.writelines(li)
        infp.close()
        outfp.close()

#调用示例
if __name__ == "__main__":
    del_blank_line("300.txt", "2.txt")