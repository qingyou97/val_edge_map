import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_arr(path):

    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    color_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    # 使用Sobel算子计算梯度
    grad_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # 计算梯度强度和方向
    magnitude = cv2.magnitude(grad_x, grad_y)
    direction = cv2.phase(grad_x, grad_y, angleInDegrees=True)


    step = 15  # 每隔多少像素绘制一个箭头

    # 遍历图像的每个像素点
    arrowed_image = color_image.copy()
    for y in range(0, image.shape[0], step):
        for x in range(0, image.shape[1], step):
            # 梯度方向
            length = 10
            angle = direction[y, x]

            # 箭头的角度和终点
            dx = int(length * np.cos(np.deg2rad(angle)))
            dy = int(length * np.sin(np.deg2rad(angle)))

            # 箭头的起点和终点
            start_point = (x, y)
            end_point = (x + dx, y + dy)

            # 用红色箭头绘制方向
            cv2.arrowedLine(arrowed_image, start_point, end_point, (0, 0, 255), 1, 8, 0, 0.3)

    cv2.imwrite('arrowed_image.png', arrowed_image)

    # 显示结果
    # plt.imshow(cv2.cvtColor(arrowed_image, cv2.COLOR_BGR2RGB))
    # plt.show()

if __name__ == '__main__':
    # 读取图像并转换为灰度图
    path = r'20241008-155135.jpg'

    plot_arr(path)
