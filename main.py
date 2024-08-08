import os
import shutil

# 定义读取图像的文件夹路径
source_folder = 'A'
# 获取文件夹里的文件列表
image_files = os.listdir(source_folder)

# 过滤掉非图像文件（可选的，根据实际需要）
image_files = [f for f in image_files if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]

for image_file in image_files:
    # 获取文件名（不包括后缀）
    folder_name = os.path.splitext(image_file)[0]
    # 定义新文件夹的路径
    new_folder_path = os.path.join(source_folder, folder_name)
    # 创建文件夹
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

print(f"创建了{len(image_files)}个文件夹")
