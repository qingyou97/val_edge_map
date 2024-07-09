import cv2
import numpy as np

# 读取图像
image = cv2.imread('your_image_path.jpg', cv2.IMREAD_GRAYSCALE) # 使用灰度模式读取图像

# 检查图像是否成功加载
if image is None:
    print("图像加载失败！请检查文件路径。")
    exit()

# 使用cv2.Laplacian检测图像边缘
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# 将图像的深度转换回来以便显示在 0-255 范围内
laplacian = np.uint8(np.absolute(laplacian))

# 显示原始图像和Laplacian边缘检测结果
cv2.imshow('Original Image', image)
cv2.imshow('Laplacian Edge Detection', laplacian)

# 等待用户关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
