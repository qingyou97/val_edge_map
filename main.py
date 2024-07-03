# 打开图片并调整大小（保持比例）
original_img = PILImage.open(img_path)
width, height = original_img.size
new_height = 20.32  # Excel中行高度，单位为“磅”，20 磅大约是2 cm
# 计算调整后的图片宽度
new_width = int(width * (new_height / height))

resized_img = original_img.resize((new_width, int(new_height)), PILImage.LANCZOS)  # 保持比例缩小图片
resized_img_path = 'resized_A.png'
resized_img.save(resized_img_path)

# 在Excel中插入调整大小后的图片
wb = load_workbook(excel_path)
sheet = wb[sheet_name]

img = Image(resized_img_path)  
sheet.add_image(img, cell)  # 指定插入位置

wb.save(excel_path)
