import os
import shutil

# 定义原本的和目标目录
source_dir = os.path.join('A')
folders = ['0_bottle', '1_casting', '2_cylinder', '3_groove', '4_aero', '5_ball_screw']

# 在A目录下创建新的文件夹
for folder in folders:
    folder_path = os.path.join(source_dir, folder)
    os.makedirs(folder_path, exist_ok=True)

    # 需要复制的文件夹
    subfolders = ['ai_result', 'gt', 'original']
    
    # 复制每个文件夹到新的文件夹里面
    for subfolder in subfolders:
        src = os.path.join(source_dir, subfolder)
        dst = os.path.join(folder_path, subfolder)
        if os.path.exists(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
