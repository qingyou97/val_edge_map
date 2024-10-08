import os
import cv2
import numpy as np

def non_max_suppression(magnitude, angle):
    M, N = magnitude.shape
    Z = np.zeros((M, N), dtype=np.int32)
    angle = angle * 180.0 / np.pi
    angle[angle < 0] += 180

    for i in range(1, M-1):
        for j in range(1, N-1):
            try:
                q = 255
                r = 255

                # angle 0
                if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                    q = magnitude[i, j+1]
                    r = magnitude[i, j-1]
                # angle 45
                elif 22.5 <= angle[i, j] < 67.5:
                    q = magnitude[i+1, j-1]
                    r = magnitude[i-1, j+1]
                # angle 90
                elif 67.5 <= angle[i, j] < 112.5:
                    q = magnitude[i+1, j]
                    r = magnitude[i-1, j]
                # angle 135
                elif 112.5 <= angle[i, j] < 157.5:
                    q = magnitude[i-1, j-1]
                    r = magnitude[i+1, j+1]

                if (magnitude[i, j] >= q) and (magnitude[i, j] >= r):
                    Z[i, j] = magnitude[i, j]
                else:
                    Z[i, j] = 0

            except IndexError as e:
                pass

    return Z

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

        # 应用高斯模糊
        blurred_img = cv2.GaussianBlur(img, (5, 5), 0)
        
        # 应用Sobel边缘检测
        sobelx = cv2.Sobel(blurred_img, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(blurred_img, cv2.CV_64F, 0, 1, ksize=3)
        magnitude = np.sqrt(sobelx**2 + sobely**2)
        angle = np.arctan2(sobely, sobelx)
        
        # 非极大值抑制
        nms_result = non_max_suppression(magnitude, angle)
        sobel_img = cv2.convertScaleAbs(nms_result)
        
        # 应用阈值处理
        _, sobel_thresh = cv2.threshold(sobel_img, 50, 255, cv2.THRESH_BINARY)
        
        # 生成新的图像名称
        name, ext = os.path.splitext(filename)
        new_filename = f"{name}_sobel_result.png"

        # 构造新的图像保存路径
        new_img_path = os.path.join(folder_path, new_filename)
        
        # 保存图像
        cv2.imwrite(new_img_path, sobel_thresh)

        print(f"Sobel结果已保存为 {new_img_path}")
