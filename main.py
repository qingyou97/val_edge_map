from PIL import Image
import numpy as np

# 打开图像
img = Image.open('你的图像文件路径.png').convert('L')

# 将图像转换为Numpy数组
pixel_values = np.array(img)

# 统计每种像素值的数量
unique, counts = np.unique(pixel_values, return_counts=True)

# 将结果转换为字典
pixel_count_dict = dict(zip(unique, counts))

print("每种像素值的数量:")
for pixel_value, count in pixel_count_dict.items():
    print(f"像素值 {pixel_value}: {count} 个像素点")
