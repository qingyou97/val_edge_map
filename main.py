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
draw.polygon([(0, 0), (cx, cy), (0, cy)], fill=colors[0])  # 左上
draw.polygon([(0, 0), (cx, cy), (cx, 0)], fill=colors[1])  # 上中
draw.polygon([(cx, 0), (cx, cy), (width, 0)], fill=colors[2])  # 右上
draw.polygon([(width, 0), (cx, cy), (width, cy)], fill=colors[3])  # 右中
draw.polygon([(width, cy), (cx, cy), (width, height)], fill=colors[4])  # 右下
draw.polygon([(cx, height), (cx, cy), (width, height)], fill=colors[5])  # 下中
draw.polygon([(0, height), (cx, cy), (cx, height)], fill=colors[6])  # 左下
draw.polygon([(0, cy), (cx, cy), (0, height)], fill=colors[7])  # 左中

# 保存或显示图像
image.show()
# image.save('output.png')
