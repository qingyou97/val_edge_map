import openpyxl

# 加载 Excel 文件
workbook = openpyxl.load_workbook("your_file.xlsx")

# 检查是否存在名称为 "A" 的工作表
if "A" in workbook.sheetnames:
    workbook.remove(workbook["A"])

# 保存修改后的文件
workbook.save("your_file.xlsx")
