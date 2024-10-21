from PIL import Image, ImageDraw

# 定义图像尺寸
width, height = 224, 224

# 创建一个新图像
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# 定义中心点
cx, cy = width // 2, height // 2

# 定义区域颜色
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'cyan']

# 画出八个区域
draw.polygon([(0, 0), (cx, 0), (cx, cy), (0, cy)], fill=colors[0])  # 左上
draw.polygon([(cx, 0), (width, 0), (width, cy), (cx, cy)], fill=colors[1])  # 右上
draw.polygon([(width, cy), (cx, cy), (cx, height), (width, height)], fill=colors[2])  # 右下
draw.polygon([(0, cy), (cx, cy), (cx, height), (0, height)], fill=colors[3])  # 左下
draw.polygon([(0, 0), (cx, 0), (cx//2, cy//2)], fill=colors[4])  # 左上小区块
draw.polygon([(cx, 0), (width, 0), (cx + cx//2, cy //2)], fill=colors[5])  # 右上小区块
draw.polygon([(0, height), (cx, height), (cx - cx//2, height - cy //2)], fill=colors[6]) # 左下小区块
draw.polygon([(cx, height), (width, height), (cx + cx//2, height - cy //2)], fill=colors[7])  # 右下小区块

# 保存或显示图像
image.show()
# image.save('output.png')
