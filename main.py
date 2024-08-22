import openpyxl
from openpyxl.drawing.image import Image
import os

# 打开工作簿和特定sheet页
workbook_path = 'your_excel_file.xlsx'
workbook = openpyxl.load_workbook(workbook_path)
sheet = workbook['1-Aero-engine-defect']

# 读取B5单元格的值
cell_value = sheet['B5'].value

# 设置图像文件夹路径
image_folder = os.path.join('A', cell_value)

# 获取图像文件列表
image_files = [file for file in os.listdir(image_folder) if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp'))]

# 检查图像数量是否达到20
if len(image_files) < 20:
    raise Exception(f"{image_folder} 只有 {len(image_files)} 张图像，不足20张。")

# 生成Excel列名
def get_excel_column_name(n):
    name = ''
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        name = chr(65 + remainder) + name
    return name

# 按照顺序将图像插入到H5、I5、J5以此类推
for index in range(20):
    image_path = os.path.join(image_folder, image_files[index])
    img = Image(image_path)
    col = get_excel_column_name(8 + index)  # 8对应H列
    img.anchor = f'{col}5'
    sheet.add_image(img)

# 保存工作簿
workbook.save(workbook_path)
