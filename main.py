import cv2
import os
from matplotlib import pyplot as plt

def binary_threshold(input_dir, threshold_value):
    # 检查阈值在合理范围内
    if threshold_value < 0 or threshold_value > 255:
        raise ValueError("阈值应在0到255范围内。")
    
    # 获取目录中的所有图像文件
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            image_path = os.path.join(input_dir, filename)
            
            # 读取图像
            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            
            if img is None:
                print(f"图像读取失败：{image_path}")
                continue
            
            # 应用二值化
            ret, binary_img = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)
            
            # 构建保存路径
            base, ext = os.path.splitext(filename)
            save_path = os.path.join(input_dir, f"{base}_threshold_{threshold_value}{ext}")
            
            # 保存二值化图像
            cv2.imwrite(save_path, binary_img)
            print(f"保存二值化图像：{save_path}")

# 示例，调整threshold_value以满足需求
binary_threshold('your_directory_path', 128)
