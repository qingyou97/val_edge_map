import cv2
import numpy as np

def resize_by_half(image):
    height, width = image.shape[:2]
    height //= 2
    width //= 2
    resized_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR) # 使用双线性插值
    return resized_image

if __name__ == "__main__":
    image_path = r"D:\\edge_detection\\code\\datasets\\metal_engine_data\\reorganization\\Metal_Training_original\\1-Aero-engine-defect\\gt_binary/4.png"
    image = cv2.imread(image_path, 0)  # 0 表示读取为灰度图像
    resized_image = resize_by_half(image)
    
    # 进行二值化处理
    _, binary_resized_image = cv2.threshold(resized_image, 127, 255, cv2.THRESH_BINARY) 

    cv2.imwrite("resized_image_cv2.jpg", binary_resized_image)
