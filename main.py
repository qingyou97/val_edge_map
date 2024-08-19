import os
import shutil

def move_files(src_folder, dst_folder_png, dst_folder_jpg):
    if not os.path.exists(dst_folder_png):
        os.makedirs(dst_folder_png)
    if not os.path.exists(dst_folder_jpg):
        os.makedirs(dst_folder_jpg)

    for file_name in os.listdir(src_folder):
        src_file = os.path.join(src_folder, file_name)
        if os.path.isfile(src_file):
            if file_name.lower().endswith('.png'):
                shutil.move(src_file, os.path.join(dst_folder_png, file_name))
            elif file_name.lower().endswith('.jpg'):
                shutil.move(src_file, os.path.join(dst_folder_jpg, file_name))

src_folder = 'A文件夹路径'
dst_folder_png = 'B文件夹路径'
dst_folder_jpg = 'C文件夹路径'

move_files(src_folder, dst_folder_png, dst_folder_jpg)
