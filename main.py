import cv2
import numpy as np

# 示例代码，用OpenCV读图和提取红色点的坐标
def extract_red_points(image_path):
    # 读取图片
    image = cv2.imread(image_path)
    # 转换为HSV颜色空间
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # 定义红色的HSV范围
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv_image, lower_red, upper_red)
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
    # 合并两个红色的mask
    red_mask = mask1 | mask2
    # 查找红色区域的轮廓
    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    red_points = [(int(contour[0][0]), int(contour[0][1])) for contour in contours]
    return red_points

# 示例B函数
def B(x, y):
    # 假设B函数接收点的坐标(x, y)，返回一个值
    return x + y  # 保持简单，这里仅为示例

# 读取并提取红点坐标
red_points = extract_red_points('A图路径')

# 将所有点坐标输入B函数，并存到新的list中
results = [B(x, y) for (x, y) in red_points]

# 计算结果list的最小值
min_value = min(results)

print(f"最小值：{min_value}")
