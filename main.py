from openpyxl import load_workbook
from openpyxl.drawing.image import Image
from PIL import Image as PILImage

# 定义文件和工作表位置等参数
img_path = 'A.png'  # 图片路径
excel_path = 'C.xlsx'  # Excel文件路径
sheet_name = 'B'  # 工作表名称
cell = 'D1'  # 图片粘贴位置

# 打开图片并调整大小（保持比例）
original_img = PILImage.open(img_path)
width, height = original_img.size
new_height = 20.32  # Excel中行高度，单位为“磅”，20 磅大约是2 cm
# 计算调整后的图片宽度
new_width = int(width * (new_height / height))

resized_img_path = 'resized_A.png'
original_img.thumbnail((new_width, new_height), PILImage.ANTIALIAS)  # 保持比例缩小图片
original_img.save(resized_img_path)

# 在Excel中插入调整大小后的图片
wb = load_workbook(excel_path)
sheet = wb[sheet_name]

img = Image(resized_img_path)  
sheet.add_image(img, cell)  # 指定插入位置

wb.save(excel_path)
