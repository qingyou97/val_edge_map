import openpyxl

# 加载 Excel 文件
workbook = openpyxl.load_workbook('your_file.xlsx')

# 获取所有 sheet 页的名字
sheet_names = workbook.sheetnames

# 打印 sheet 页名字列表
print(sheet_names)
