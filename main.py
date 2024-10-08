import os
import shutil

# 源文件夹A的路径
source_folder = 'A文件夹路径'
# 目标文件夹B的路径
dest_folder = 'B文件夹路径'

# 确保目标文件夹存在
os.makedirs(dest_folder, exist_ok=True)

for root, dirs, files in os.walk(source_folder):
    for dir_name in dirs:
        segmentation_images_path = os.path.join(root, dir_name, 'segmentation_images')
        if os.path.exists(segmentation_images_path):
            for image_name in os.listdir(segmentation_images_path):
                image_path = os.path.join(segmentation_images_path, image_name)
                if os.path.isfile(image_path):  # 确保这是一个文件
                    new_image_name = f"{os.path.basename(source_folder)}_{dir_name}_{image_name}"
                    new_image_path = os.path.join(dest_folder, new_image_name)
                    shutil.copyfile(image_path, new_image_path)
