import os
import shutil

# 定义路径
A_folder = 'A'  # 修改为实际 A 文件夹的路径
B_folder = 'B'  # 修改为实际 B 文件夹的路径
C_folder = 'C'  # 修改为实际 C 文件夹的路径
D_folder = 'D'  # 修改为实际 D 文件夹的路径

# 创建B, C, D文件夹 如果它们不存
os.makedirs(B_folder, exist_ok=True)
os.makedirs(C_folder, exist_ok=True)
os.makedirs(D_folder, exist_ok=True)

# 初始item从1开始
item = 1

# 遍历A文件夹下的所有子文件夹
for sub_folder in os.listdir(A_folder):
    sub_folder_path = os.path.join(A_folder, sub_folder)
    
    # 确认此路径是一个文件夹
    if os.path.isdir(sub_folder_path):
        segmentation_images_folder = os.path.join(sub_folder_path, 'segmentation_images')
        
        if os.path.exists(segmentation_images_folder):
            # src为原文件路径，dest为新路径（包括重命名）
            query_img_src = os.path.join(segmentation_images_folder, 'query_img.png')
            mask_img_src = os.path.join(segmentation_images_folder, 'mask_img.png')
            merged_binary_src = os.path.join(segmentation_images_folder, 'merged_binary.png')
            
            if os.path.exists(query_img_src) and os.path.exists(mask_img_src) and os.path.exists(merged_binary_src):
                query_img_dest = os.path.join(B_folder, f'{item}_original.png')
                mask_img_dest = os.path.join(C_folder, f'{item}_gt.png')
                merged_binary_dest = os.path.join(D_folder, f'{item}_ai_result.png')

                # 移动并重命名文件
                shutil.copy(query_img_src, query_img_dest)
                shutil.copy(mask_img_src, mask_img_dest)
                shutil.copy(merged_binary_src, merged_binary_dest)

                # 每次运行完成之前item加1
                item += 1
