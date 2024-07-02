import os
import shutil

def move_png_images(a_folder):
    # 创建B文件夹名，通过在A文件夹名后添加 "_png" 尾缀
    b_folder = a_folder.rstrip('/') + '_png'

    # 如果B文件夹不存在，则创建B文件夹
    if not os.path.exists(b_folder):
        os.makedirs(b_folder)
    
    # 遍历A文件夹中的文件
    for filename in os.listdir(a_folder):
        # 检查文件扩展名是否为png
        if filename.endswith('.png'):
            # 构建源文件路径和目标文件路径
            src_path = os.path.join(a_folder, filename)
            dst_path = os.path.join(b_folder, filename)
            # 移动文件
            shutil.move(src_path, dst_path)
            print(f'Moved: {src_path} to {dst_path}')

# 调用函数并传入A文件夹路径
move_png_images('path_to_A_folder')
