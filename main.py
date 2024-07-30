import openpyxl
from openpyxl.drawing.image import Image

# 打开 Excel 文件
wb = openpyxl.load_workbook('A.xlsx')

# 选择特定的工作表
ws = wb['B']

# 获取所有图像
images_to_remove = []
for image in ws._images:
    # 获取图像的起始行
    start_row = image.anchor._from.row
    if start_row == 8:
        images_to_remove.append(image)

# 删除图像
for image in images_to_remove:
    ws._images.remove(image)

# 保存 Excel 文件
wb.save('A_modified.xlsx')
