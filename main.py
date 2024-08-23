import os
import shutil

# 源文件夹列表
source_folders = ['A', 'B', 'C', 'D', 'E']
# 目标文件夹
target_folder = 'F'

# 确保目标文件夹存在
os.makedirs(target_folder, exist_ok=True)

# 遍历每个源文件夹
for folder in source_folders:
    source_image_folder = os.path.join(folder, 'image_512')
    # 如果源文件夹存在
    if os.path.exists(source_image_folder):
        # 遍历每个文件
        for file_name in os.listdir(source_image_folder):
            source_file = os.path.join(source_image_folder, file_name)
            # 如果是文件
            if os.path.isfile(source_file):
                # 新文件名
                new_file_name = f"{folder}_{file_name}"
                target_file = os.path.join(target_folder, new_file_name)
                # 复制文件到目标文件夹
                shutil.copy2(source_file, target_file)
