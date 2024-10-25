# 定义扩散范围
range_size = 4

# 提高所有坐标点及其周围像素的对比度
for (x, y) in coordinates:
    for i in range(-range_size, range_size + 1):
        for j in range(-range_size, range_size + 1):
            if 0 <= x + i < image.shape[1] and 0 <= y + j < image.shape[0]:
                image[y + j, x + i] = min(255, image[y + j, x + i] * 2)
