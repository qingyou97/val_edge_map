import os
import random
import shutil

# 源目录和目标目录
src_dir = 'source_directory_path'  # 更改为你的图像文件夹路径
dst_dir = 'destination_directory_path'  # 更改为你的目标文件夹路径

# 获取所有文件名并按前缀分组
groups = {}
for filename in os.listdir(src_dir):
    if filename.endswith('.png'):
        prefix = '_'.join(filename.split('_')[:3])
        if prefix not in groups:
            groups[prefix] = []
        groups[prefix].append(filename)

# 从每组中随机选择一张图像，并复制到目标文件夹
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

for group in groups.values():
    chosen_file = random.choice(group)
    shutil.copy(os.path.join(src_dir, chosen_file), os.path.join(dst_dir, chosen_file))

print(f"选出的图像已复制到 {dst_dir} 文件夹中。")
