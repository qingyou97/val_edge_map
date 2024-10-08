import os
from PIL import Image
import numpy as np

# 文件夹路径
gt_folder = 'C'
result_folder = 'D'
output_folder = 'E'

# 创建输出文件夹，如果不存在的话
os.makedirs(output_folder, exist_ok=True)

# 获取文件列表
gt_files = {f.split('_')[0]: f for f in os.listdir(gt_folder) if f.endswith('_gt.png')}
result_files = {f.split('_')[0]: f for f in os.listdir(result_folder) if f.endswith('_result_sobel_result.png')}

# 处理每一对文件
for key in gt_files.keys():
    if key in result_files:
        gt_path = os.path.join(gt_folder, gt_files[key])
        result_path = os.path.join(result_folder, result_files[key])
        
        # 加载图像
        gt_image = Image.open(gt_path).convert('RGB')
        result_image = Image.open(result_path).convert('RGB')
        
        # 转换成numpy数组
        gt_np = np.array(gt_image)
        result_np = np.array(result_image)
        
        # 创建红色注释图层
        red = np.array([255, 0, 0])
        
        # 找到gt_image中不是黑色的像素点
        mask = (gt_np != [0, 0, 0]).any(axis=-1)
        
        # 在result_image中用红色标注这些点
        result_np[mask] = red
        
        # 保存新图像
        output_image = Image.fromarray(result_np)
        output_path = os.path.join(output_folder, f'{key}_highlighted.png')
        output_image.save(output_path)

        print(f"Processed and saved: {output_path}")
