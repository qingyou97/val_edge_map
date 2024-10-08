import os
from PIL import Image

def crop_images(input_folder, output_folder, top_left_x, top_left_y, width, height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            cropped_img = img.crop((top_left_x, top_left_y, top_left_x + width, top_left_y + height))
            cropped_img.save(os.path.join(output_folder, filename))

# 通用参数
input_folder = 'A'  # 源文件夹路径
output_folder = 'B'  # 目标文件夹路径
top_left_x = 39  # 裁剪框的左上角横坐标
top_left_y = 23  # 裁剪框的左上角纵坐标
width = 250  # 裁剪宽度
height = 250  # 裁剪高度

crop_images(input_folder, output_folder, top_left_x, top_left_y, width, height)
