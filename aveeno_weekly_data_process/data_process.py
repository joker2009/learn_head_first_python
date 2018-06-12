import openpyxl

excel = openpyxl.load_workbook(r'E:\learn_head_first_python\aveeno_weekly_data_process\Aveeno产品JB条码周报20180604-0610(1).xlsx')
a = excel.active
b = excel.worksheets
print(a)
print(b)