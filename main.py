import os
import shutil

# 定义A和B文件夹路径
A_folder = 'path_to_A_folder'
B_folder = 'path_to_B_folder'

# 获取A文件夹下所有子文件夹
subfolders = [f.name for f in os.scandir(A_folder) if f.is_dir()]

# 遍历每个子文件夹
for subfolder in subfolders:
    A_subfolder_path = os.path.join(A_folder, subfolder)
    B_subfolder_path = os.path.join(B_folder, subfolder)

    # 如果B文件夹下对应的子文件夹不存在，则创建
    if not os.path.exists(B_subfolder_path):
        os.makedirs(B_subfolder_path)

    # 复制A子文件夹中的指定子文件夹（test_gt 和 test_images）到B对应的子文件夹
    for subdir in ['test_gt', 'test_images']:
        source_path = os.path.join(A_subfolder_path, subdir)
        dest_path = os.path.join(B_subfolder_path, subdir)
        if os.path.exists(source_path):
            if os.path.exists(dest_path):
                shutil.rmtree(dest_path)  # 如果目标路径已存在，先删除
            shutil.copytree(source_path, dest_path)

print("复制完成")
