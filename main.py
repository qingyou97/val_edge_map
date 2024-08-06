from PIL import Image
import numpy as np

# 打开图像
img = Image.open('你的图像文件路径.png').convert('L')

# 将图像转换为Numpy数组
pixel_values = np.array(img)

# 获取唯一的像素值
unique_values = np.unique(pixel_values)

print("图像中唯一像素值有:", unique_values)
