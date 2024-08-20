import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

# 示例二维图像（可以用你自己的图像替换）
image = np.random.rand(10, 10)

# 缩放到原来的一半
zoom_factors = (0.5, 0.5)  # 对应行和列方向的缩放因子
scaled_image = ndi.zoom(image, zoom_factors, order=0)  # order=0 表示最近邻插值

# 保存缩放后的图像到本地
plt.imsave('scaled_image.png', scaled_image, cmap='gray')
