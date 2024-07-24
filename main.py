import os
import shutil

def find_and_copy_images(A_folder, B_folder):
    # 获取A文件夹中的所有子文件夹
    for subdir in os.listdir(A_folder):
        subdir_path = os.path.join(A_folder, subdir)
        
        # 确保这是一个文件夹
        if os.path.isdir(subdir_path):
            parts = subdir.split('_')
            first_part = parts[0]
            rest_part = '_'.join(parts[1:])
            
            # 构建源路径和目标路径
            src_folder = os.path.join(B_folder, first_part, 'ground_truth', rest_part)
            dest_folder = os.path.join(subdir_path, 'test_gt')
            
            # 确保源路径存在
            if os.path.exists(src_folder):
                # 创建目标文件夹，如果不存在的话
                os.makedirs(dest_folder, exist_ok=True)
                
                # 复制图像
                for file_name in os.listdir(src_folder):
                    src_file = os.path.join(src_folder, file_name)
                    dest_file = os.path.join(dest_folder, file_name)
                    if os.path.isfile(src_file):
                        shutil.copy(src_file, dest_file)
                print(f"Copied images from {src_folder} to {dest_folder}")
            else:
                print(f"Source folder {src_folder} does not exist")

# 使用示例
A_folder = '/path/to/A_folder'
B_folder = '/path/to/B_folder'
find_and_copy_images(A_folder, B_folder)
