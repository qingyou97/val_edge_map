from PIL import Image

# 打开图像A和图像B
imgA = Image.open("A.png").convert("1")  # 转换为黑白图
imgB = Image.open("B.png").convert("1")  # 转换为黑白图

# 创建一个新的图像用于结果展示，RGB模式
result = Image.new("RGB", imgA.size)

# 获取像素数据
pixelsA = imgA.load()
pixelsB = imgB.load()
pixelsResult = result.load()

for x in range(imgA.width):
    for y in range(imgA.height):
        if pixelsA[x, y] == 255:  # 图A上的白色像素
            if pixelsB[x, y] == 255:  # 在图B上也是白色像素
                pixelsResult[x, y] = (0, 0, 255)  # 蓝色标记重叠区域
            else:
                pixelsResult[x, y] = (255, 255, 255)  # 白色标记图A上的像素
        elif pixelsB[x, y] == 255:
            pixelsResult[x, y] = (255, 0, 0)  # 红色标记图B上的像素
        else:
            pixelsResult[x, y] = (0, 0, 0)  # 黑色背景

# 保存结果图像
result.save("result.png")

# 如果需要显示图像，可以使用以下代码
result.show()
