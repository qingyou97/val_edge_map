import os
import random
from collections import defaultdict

# 源文件夹路径
src_folder = r'D:\1_code_project\1_CV\4_Keyence\testdata'
# 目标文件夹路径
dst_folder = r"./select"  # 替换成实际路径

import os
import shutil

def clear_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

folder_path = dst_folder
clear_folder(folder_path)

# 创建目标文件夹（如果尚未创建）
os.makedirs(dst_folder, exist_ok=True)

# 存储按前缀分组的图像文件
prefix_dict = defaultdict(list)

# 遍历源文件夹中的所有图像文件
for filename in os.listdir(src_folder):
    if filename.endswith(".png"):
        prefix = filename.split('_')[0]
        prefix_dict[prefix].append(filename)

# 在每组内随机选择一张图像保存到目标文件夹
for prefix, files in prefix_dict.items():
    if len(files) > 0:
        selected_file = random.choice(files)
        src_path = os.path.join(src_folder, selected_file)
        dst_path = os.path.join(dst_folder, selected_file)
        os.rename(src_path, dst_path)  # 也可以使用shutil.move(src_path, dst_path)

print(f"已经从每组内随机选出一张图像，并保存到 {dst_folder}")
