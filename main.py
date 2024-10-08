import os
import cv2
import numpy as np

# 指定文件夹A的路径
folder_path = 'A'

# 遍历文件夹A里的所有文件
for filename in os.listdir(folder_path):
    if 'original' in filename:
        # 构造图像的完整路径
        img_path = os.path.join(folder_path, filename)
        
        # 读取图像
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        
        # 确认图像被正确加载
        if img is None:
            print(f"图像文件 {img_path} 读取失败")
            continue

        # 应用Sobel边缘检测
        sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
        sobel_mag = np.sqrt(sobelx**2 + sobely**2)
        sobel_img = cv2.convertScaleAbs(sobel_mag)
        
        # 生成新的图像名称
        new_filename = filename.replace('original', 'sobel_result') + '.png'

        # 构造新的图像保存路径
        new_img_path = os.path.join(folder_path, new_filename)
        
        # 保存图像
        cv2.imwrite(new_img_path, sobel_img)

        print(f"Sobel结果已保存为 {new_img_path}")
