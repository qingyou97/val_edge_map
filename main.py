import os
import shutil

A_folder = '路径到A文件夹'
B_folder = '路径到B文件夹'
C_folder = '路径到C文件夹'

# 确保C文件夹存在
if not os.path.exists(C_folder):
    os.makedirs(C_folder)

# 获取A文件夹中的图像名称
image_names = os.listdir(A_folder)

# 从B文件夹复制对应的图像到C文件夹
for image_name in image_names:
    src_path = os.path.join(B_folder, image_name)
    dest_path = os.path.join(C_folder, image_name)
    # 确保图像在B文件夹中存在
    if os.path.exists(src_path):
        shutil.copy(src_path, dest_path)
    else:
        print(f"图像 {image_name} 在B文件夹中不存在")

print("复制完成")
