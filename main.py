import cv2
import numpy as np

def find_and_draw_most_circular_ellipse(image_path, output_path):
    # 读取图像
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 使用开闭运算进行处理
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

    # 阈值分割
    _, binary_image = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)

    # Laplace变换找到轮廓线
    laplacian_kernel = np.array([[0, 1, 0], 
                                 [1, -4, 1], 
                                 [0, 1, 0]], dtype=float)
    laplacian_output = cv2.filter2D(binary_image, cv2.CV_32F, laplacian_kernel)
    laplacian_output = np.uint8(np.absolute(laplacian_output))

    # 查找轮廓
    contours, _ = cv2.findContours(laplacian_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 原图转换为BGR彩色图像
    original_image = cv2.imread(image_path)
    if original_image.ndim == 2:
        original_image = cv2.cvtColor(original_image, cv2.COLOR_GRAY2BGR)

    # 提取合适的轮廓并拟合椭圆
    best_ellipse = None
    best_ratio = float('inf')  # 初始化为无穷大

    for contour in contours:
        if len(contour) < 5:  # 拟合椭圆需要的点数最少为 5
            continue
        ellipse = cv2.fitEllipse(contour)
        (center, axes, angle) = ellipse
        major_axis = max(axes)
        minor_axis = min(axes)
        ratio = major_axis / minor_axis
        
        if ratio < best_ratio:
            best_ratio = ratio
            best_ellipse = ellipse

    # 绘制最圆的椭圆和圆心
    if best_ellipse is not None:
        color = (0, 255, 0)  # 绿色
        cv2.ellipse(original_image, best_ellipse, color, 2)
        center = best_ellipse[0]  # 圆心坐标
        center = (int(center[0]), int(center[1]))  # 转换为整数坐标
        cv2.circle(original_image, center, 5, color, -1)  # 绘制圆心
    else:
        center = None

    # 保存结果图像
    cv2.imwrite(output_path, original_image)

    return center

# 使用示例
image_path = 'path_to_image'
output_path = 'output_path'
center = find_and_draw_most_circular_ellipse(image_path, output_path)
if center is not None:
    print(f"最圆的椭圆的圆心坐标为: {center}")
else:
    print("未找到合适的椭圆")
