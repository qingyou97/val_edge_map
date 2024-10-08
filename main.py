import os
from PIL import Image

# 定义文件夹路径
A_folder = "A文件夹路径"
B_folder = "B文件夹路径"

if not os.path.exists(B_folder):
    os.makedirs(B_folder)

# 处理A文件夹中的所有图像
for filename in os.listdir(A_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        file_path = os.path.join(A_folder, filename)
        img = Image.open(file_path)
        
        # 获取图像尺寸
        width, height = img.size
        
        # 裁剪图像 （横向只保留最后80像素）
        left = width - 80
        right = width
        top = 0
        bottom = height
        cropped_img = img.crop((left, top, right, bottom))
        
        #保存到B文件夹
        cropped_img.save(os.path.join(B_folder, filename))

print("所有图片已裁剪并保存到B文件夹。")
