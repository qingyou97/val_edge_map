import os
from PIL import Image

def check_image_size(folder_path):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 构造文件的完整路径
        file_path = os.path.join(folder_path, filename)
        try:
            # 打开图像文件
            with Image.open(file_path) as img:
                # 检查图像尺寸是否为900x900
                if img.size != (900, 900):
                    print(f"{filename} 的尺寸不是900x900，而是 {img.size}")
        except (IOError, SyntaxError) as e:
            print(f"无法处理文件 {file_path}: {e}")

# 设置要检查的文件夹路径
folder_path = "A"
check_image_size(folder_path)
