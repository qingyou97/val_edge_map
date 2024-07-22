import os
import shutil

# 设置文件夹路径
folder_A = "path_to_A"
folder_B = "path_to_B"
folder_C = "path_to_C"

# 获取A文件夹里的文件列表
files_A = os.listdir(folder_A)

# 确保C文件夹存在
os.makedirs(folder_C, exist_ok=True)

# 遍历A文件夹里的文件
for file_A in files_A:
    file_B_path = os.path.join(folder_B, file_A)
    
    # 检查B文件夹中是否存在同名文件
    if os.path.isfile(file_B_path):
        # 如果存在，移动到C文件夹
        shutil.copy(file_B_path, folder_C)

print("文件移动完成")
