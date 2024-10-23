from PIL import Image

# 打开 A 图和 B 图
a_image = Image.open('A.png')
b_image = Image.open('B.png')

# 加载像素
a_pixels = a_image.load()
b_pixels = b_image.load()

# 遍历检查每个像素
width, height = a_image.size
red_points = []
for x in range(width):
    for y in range(height):
        if a_pixels[x, y] == (255, 0, 0):  # 查找正红色点
            red_points.append((x, y))
            b_pixels[x, y] = (255, 0, 0)  # 在 B 图上涂上红色

# 保存 B 图
b_image.save('B_with_red.png')
