from PIL import Image
from collections import Counter

# 打开图像
image_path = "path_to_your_image.jpg"
image = Image.open(image_path)

# 获取图像尺寸
width, height = image.size
print(f"图像尺寸: {width}x{height}")

# 获取所有像素的RGB值
pixels = list(image.getdata())

# 计算不同像素值的数量和总计
counter = Counter(pixels)
total_pixels = sum(counter.values())

print(f"总像素数: {total_pixels}")
print("各像素值的数量如下:")

for pixel_value, count in counter.items():
    print(f"RGB值: {pixel_value}, 数量: {count}")
