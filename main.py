import os
import shutil

# 替换为你要清空的文件夹路径
folder_path = "A"

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        os.remove(file_path)
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        shutil.rmtree(dir_path)
        os.makedirs(dir_path)
