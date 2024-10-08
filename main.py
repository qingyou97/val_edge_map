import cv2
import numpy as np
from skimage.morphology import skeletonize

# 读取图像
img = cv2.imread(r"D:\\edge_detection\\code\\magnitudee\\main_image\\ai_result\\12_result.png")

# 转为灰度图像
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 高斯模糊
img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)

# Otsu阈值二值化
ret, img_thresh = cv2.threshold(img_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 形态学操作：开运算（去除小的白色噪点）
kernel = np.ones((3, 3), np.uint8)
img_open = cv2.morphologyEx(img_thresh, cv2.MORPH_OPEN, kernel)

# 形态学操作：闭运算（填充小的黑色空洞）
img_close = cv2.morphologyEx(img_open, cv2.MORPH_CLOSE, kernel)

# 细线化(骨架化)
ske = skeletonize(img_close == 0)  # 注意要确保图像对比度，可能要反转
ske_gray = (ske * 255).astype(np.uint8)

# 转为RGB图像
ske_rgb = cv2.cvtColor(ske_gray, cv2.COLOR_GRAY2BGR)

# 显示结果
cv2.imshow('Skeletonized Image', ske_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
