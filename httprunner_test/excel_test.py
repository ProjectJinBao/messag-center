import xlrd
import xlutils
import xlwt
from xlutils.copy import copy

filename = '/Users/yujing/Desktop/测试/测试用例/DX-DMP测试用例.xlsx'
workbook = xlrd.open_workbook(filename)#保留原excel格式
table = workbook.sheet_by_name('API网关')#获取名字为API网关的sheet对象
names = workbook.sheet_names()#获取所以sheet的名字
row_num = table.nrows #获取有效行数
clos_num = table.ncols #获取有效列数
dat = table.cell_value(0, 0)#获取单元格的值
print(dat)

new_data = copy(workbook)
table_new = new_data.get_sheet('API网关')
table_new.write(2,0,"ee")
new_data.save("ee.xls")


