import os

import json
import numpy as np
import cv2


def json2mask(folder_path, mask_folder_path):
    if not os.path.exists(mask_folder_path):
        os.makedirs(mask_folder_path, exist_ok=True)

    json_list = os.listdir(folder_path)
    for name in json_list:
        json_path = os.path.join(folder_path, name)
        suffix = name.split('.')[-1]
        if suffix in ['json']:
            # 读取JSON文件
            with open(json_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            # 获取图像路径和尺寸
            image_path = data['imagePath']
            image_height = data['imageHeight']
            image_width = data['imageWidth']

            # 创建一个空白的黑白二值图（全为零，表示黑色）
            binary_image = np.zeros((image_height, image_width), dtype=np.uint8)

            # 获取点的列表
            for shape in data['shapes']:
                points = shape['points']
                points = np.array(points, np.int32)
                points = points.reshape((-1, 1, 2))

                # 画线
                cv2.polylines(binary_image, [points], isClosed=False, color=255, thickness=1)
            mask_path = os.path.join(mask_folder_path, rf"{name.split('.')[0]}.png")
            print(f'mask pixel value: {set(list(binary_image.flatten()))}')
            # 保存生成的图像
            cv2.imwrite(mask_path, binary_image)

if __name__ == '__main__':
    json_path = r'E:\1\json'
    mask_folder_path = r'mask'
    json2mask(json_path, mask_folder_path)

    
