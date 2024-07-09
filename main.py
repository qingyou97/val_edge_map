import cv2

# 读取图像
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# 可选：降噪处理
blurred_image = cv2.GaussianBlur(image, (5, 5), 1.4)

# Canny边缘检测
edges = cv2.Canny(blurred_image, threshold1=50, threshold2=150)

# 显示结果
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
