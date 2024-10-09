import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def find_peak_magnitude(magnitude, angle, y, x):
    M, N = magnitude.shape
    peak_coordinates = []

    angle_deg = angle[y, x] * 180.0 / np.pi
    angle_deg = angle_deg if angle_deg >= 0 else angle_deg + 180

    # Define directions based on angle
    if (0 <= angle_deg < 22.5) or (157.5 <= angle_deg < 180):
        directions = [(0, 1), (0, -1)]  # 0 degrees, horizontal direction
    elif 22.5 <= angle_deg < 67.5:
        directions = [(1, -1), (-1, 1)]  # 45 degrees
    elif 67.5 <= angle_deg < 112.5:
        directions = [(1, 0), (-1, 0)]  # 90 degrees, vertical direction
    else:
        directions = [(1, 1), (-1, -1)]  # 135 degrees

    for dx, dy in directions:
        step = 1
        while True:
            new_x = x + step * dx
            new_y = y + step * dy

            if not (0 <= new_x < N and 0 <= new_y < M):
                break

            if magnitude[new_y, new_x] == 0:
                stop_count = 1
                while stop_count < 5:
                    step += 1
                    new_x = x + step * dx
                    new_y = y + step * dy
                    if not (0 <= new_x < N and 0 <= new_y < M) or magnitude[new_y, new_x] != 0:
                        break
                    stop_count += 1
                if stop_count == 5:
                    break

            peak_coordinates.append((new_y, new_x, magnitude[new_y, new_x]))
            step += 1

    return peak_coordinates

def plot_peak_coordinates(peak_coordinates, ix, iy):
    coords = [(i[1], i[0]) for i in peak_coordinates]  # x, y
    intensities = [i[2] for i in peak_coordinates]

    plt.figure()
    if len(peak_coordinates) > 1:
        max_intensity_index = np.argmax(intensities)
        plt.plot([c[0] for c in coords], intensities, marker='o')
        plt.text(coords[max_intensity_index][0], intensities[max_intensity_index], f"Max: {coords[max_intensity_index]}", fontsize=12, color='red')
    
        plt.title('Intensity Profile')
        plt.xlabel('Pixel X-coordinate')
        plt.ylabel('Intensity Value')

        plt.grid()
        plt.show()

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

        # 替换使用改进的峰值搜索
        peak_coordinates = find_peak_magnitude(magnitude, angle, *[(100, 100)])  # Replace with desired i, j points

        # 画出结果
        plot_peak_coordinates(peak_coordinates, 100, 100)
