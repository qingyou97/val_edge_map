import cv2
import numpy as np

def resize_by_half(image):
    height, width = image.shape[:2]
    height //= 2
    width //= 2
    
    # 形态学操作：膨胀和腐蚀
    kernel = np.ones((3, 3), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.erode(image, kernel, iterations=1)
    
    # 使用最近邻插值法
    image = cv2.resize(image, (width, height), interpolation=cv2.INTER_NEAREST)
    return image

if __name__ == "__main__":
    image_path = r"D:\\edge_detection\\code\\datasets\\metal_engine_data\\reorganization\\Metal_Training_original\\1-Aero-engine-defect\\gt_binary\\4.png"
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if image is not None:
        resized_image = resize_by_half(image)
        cv2.imwrite("resized_image_cv2.jpg", resized_image)
    else:
        print("无法读取图片")
