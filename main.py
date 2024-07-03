from openpyxl import Workbook
from openpyxl.drawing.image import Image as XLImage
from PIL import Image as PILImage

# 打开Excel文件或创建新工作簿
wb = Workbook()
ws = wb.active
ws.title = "B页"

# 打开要粘贴的图片
img_path = 'A图片路径.jpg'
img = PILImage.open(img_path)

# 获取并保持图片横纵比，缩小到高为2
# 假设高为2是以某固定单位，比如厘米
required_height_cm = 2
width, height = img.size

# 高度转换为像素（假设设置100DPI，对于60DPI价值最大）：
dpi = 100
required_height_pixels = required_height_cm * dpi / 2.54

if height > required_height_pixels:
    resize_ratio = required_height_pixels / height
    new_size = (int(width * resize_ratio), int(height * resize_ratio))
    img = img.resize(new_size, PILImage.ANTIALIAS)

# 保存调整后的图片到临时文件
temp_img_path = 'temp.jpg'
img.save(temp_img_path)

# 插入图片到Excel指定位置C位置
excel_img = XLImage(temp_img_path)
ws.add_image(excel_img, 'C1')  # 说明："C1" 是Excel的位置

# 保存Excel文件
wb.save('path_to_your_excel_file.xlsx')

# 删除临时文件（如果需要）
import os
os.remove(temp_img_path)
