import os

# 文件夹路径
folder_path = 'A'  # 请将'A'替换为你的实际路径

# 获取所有文件夹名称
subfolders = [f.name for f in os.scandir(folder_path) if f.is_dir()]

print(subfolders)
