import os
from PIL import Image

def resize_images(folder_path, output_folder, size=(512, 512)):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        img_path = os.path.join(folder_path, filename)
        with Image.open(img_path) as img:
            img = img.resize(size)
            img.save(os.path.join(output_folder, filename))

# 定义输入和输出文件夹
a_folder = 'A文件夹路径'
b_folder = 'B文件夹路径'
a_output = 'A_output'
b_output = 'B_output'

# 调用函数处理A和B文件夹
resize_images(a_folder, a_output)
resize_images(b_folder, b_output)
