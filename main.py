import openpyxl
from openpyxl.drawing.image import Image

# 打开 Excel 文件
wb = openpyxl.load_workbook('A.xlsx')

# 选择特定的工作表
ws = wb['B']

#缓存待删除Ploc 图片的位置
image_positions = []
for image in ws._images:
    if image.anchor._from[2] == 7:
        image_positions.append(image)
        
# 删除表格canvas实体
for pos in image_positions:
    ws._images.remove(pos)

# 保存 Excel 文件
wb.save('A_modified.xlsx')
