import os
import random
import shutil

# 设置图像文件夹路径
image_folder = "<图像文件夹的完整路径>"  # 替换成实际路径
output_folder = "<输出文件夹的完整路径>"  # 替换成实际路径

# 创建输出文件夹，如果文件夹不存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 提取组别信息
image_dict = {}
for filename in os.listdir(image_folder):
    if filename.endswith('.png'):
        group_key = '_'.join(filename.split('_')[:3])
        if group_key not in image_dict:
            image_dict[group_key] = []
        image_dict[group_key].append(filename)

# 从每一组中随机选择一个文件
for group_key, files in image_dict.items():
    random_file = random.choice(files)
    source_path = os.path.join(image_folder, random_file)
    destination_path = os.path.join(output_folder, random_file)
    shutil.copy2(source_path, destination_path)

print("任务完成，共选择了100张图片")
