import openpyxl
import os
from PIL import Image as PilImage
from openpyxl.drawing.image import Image as OpenpyxlImage

# 读取Excel文件
excel_file = 'path/to/excel/file.xlsx'
wb = openpyxl.load_workbook(excel_file)
sheet = wb['1-Aero-engine-defect']

# 读取B5格中的字符串
folder_name = sheet['B5'].value   # 示例值：14_2_epoch50

# 文件夹路径
base_path = 'path/to/A_folder/'   # A文件夹的路径
target_folder_path = os.path.join(base_path, folder_name)

# 基础列标题生成函数
def generate_excel_columns():
    columns = []
    for i in range(ord('H'), ord('Z') + 1):
        columns.append(chr(i))
    for i in range(ord('A'), ord('Z') + 1):
        for j in range(ord('A'), ord('Z') + 1):
            columns.append(chr(i) + chr(j))
    return columns

columns = generate_excel_columns()
images = os.listdir(target_folder_path)[:20]  # 获取目标文件夹中前20个文件名

row = 5

for count, image_name in enumerate(images):
    col_letter = columns[count]
    
    # 设置图片名字到表格中
    cell_name = f'{col_letter}{row-1}'  # 图片名插入该单元格
    sheet[cell_name] = image_name  # 粘贴图像名字到这个格
    
    # 读取并粘贴图像
    image_path = os.path.join(target_folder_path, image_name)
    img = OpenpyxlImage(image_path)
    img.anchor = f'{col_letter}{row}'
    sheet.add_image(img)  # 粘贴图像到该单元格后面
    
# 保存Excel文件
wb.save('path/to/save/new_excel_file.xlsx')
