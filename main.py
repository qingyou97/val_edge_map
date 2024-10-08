import cv2
import numpy as np
from collections import Counter

# 读取原始图像
image = cv2.imread('your_image.png')

# 将图像转换为一维数组
pixels = image.reshape(-1, 3)

# 统计每个颜色的出现次数
color_counts = Counter(map(tuple, pixels))

# 找到出现次数最多的颜色
most_common_color = color_counts.most_common(1)[0][0]

# 创建掩膜，将最常见的颜色变为黑色
mask = np.all(image == most_common_color, axis=-1)
image[mask] = [0, 0, 0]

# 将其他颜色变为白色
image[~mask] = [255, 255, 255]

# 保存最终图像
cv2.imwrite('result_image.png', image)
