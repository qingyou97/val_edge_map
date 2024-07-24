import os
import shutil

# 定义A、B目录路径
A_dir = '/path/to/A'
B_dir = '/path/to/B'

def copy_images(A_folder_name):
    components = A_folder_name.split('_')
    main_folder = components[0]
    sub_folder = '_'.join(components[1:])
    
    B_source_folder = os.path.join(B_dir, main_folder, 'ground_truth', sub_folder)
    A_target_folder = os.path.join(A_dir, A_folder_name)
    
    if os.path.exists(B_source_folder):
        for filename in os.listdir(B_source_folder):
            # 完整文件路径
            source_file = os.path.join(B_source_folder, filename)
            if os.path.isfile(source_file):
                # 复制文件
                shutil.copy(source_file, A_target_folder)
                print(f"Copied {source_file} to {A_target_folder}")
    else:
        print(f"Source folder {B_source_folder} does not exist")

# 遍历A目录下的所有文件夹并复制图像
for folder_name in os.listdir(A_dir):
    A_folder_path = os.path.join(A_dir, folder_name)
    if os.path.isdir(A_folder_path):
        copy_images(folder_name)
