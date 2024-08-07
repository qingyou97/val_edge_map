import os
from collections import Counter
from PIL import Image

def analyze_images(folder_path):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        # 确保是图像文件
        if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff')):
            image = Image.open(file_path).convert('L')  # 将图像转换为灰度图
            pixel_values = list(image.getdata())
            
            pixel_count = Counter(pixel_values)
            unique_pixels = len(pixel_count.keys())
            
            print(f"文件: {file_name}")
            print(f"共有{unique_pixels}种像素值")
            for pixel_val, count in pixel_count.items():
                print(f"像素值 {pixel_val} : {count} 个")
            print("-" * 40)

# 指定A文件夹路径
folder_path = '路径到A文件夹'
analyze_images(folder_path)
