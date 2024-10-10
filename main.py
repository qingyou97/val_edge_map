import cv2
import os
import numpy as np

# 获取文件夹路径
dir_A = '路径到文件夹A'
dir_B = '路径到文件夹B'

# 获取文件名列表
files_A = [f for f in os.listdir(dir_A) if f.endswith('.jpg')]
files_B = [f for f in os.listdir(dir_B) if f.endswith('.png')]

# 确保 A 和 B 的文件名对应
files_A.sort()
files_B.sort()

for file_A in files_A:
    # 构造B文件名
    file_base_name = os.path.splitext(file_A)[0]
    file_B = file_base_name + '.png'

    if file_B in files_B:
        # 加载图像
        img_A = cv2.imread(os.path.join(dir_A, file_A))
        img_B = cv2.imread(os.path.join(dir_B, file_B), cv2.IMREAD_GRAYSCALE)

        # 找到白色点位置
        white_points = np.argwhere(img_B == 255)

        # 在图像A标注红点
        for point in white_points:
            cv2.circle(img_A, (point[1], point[0]), 1, (0, 0, 255), -1)

        # 保存标注后的图像
        output_path = os.path.join(dir_A, 'marked_' + file_A)
        cv2.imwrite(output_path, img_A)
        
        print(f"Processed: {file_A} with {file_B}, saved to {output_path}")
    else:
        print(f"No matching file found for {file_A}")

print("Completed all processing.")
