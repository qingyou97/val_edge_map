from PIL import Image, ImageDraw, ImageShow
import numpy as np

def divide_and_color_image(image_path):
    # 打开图片
    img = Image.open(image_path)
    w, h = img.size

    # 确保图片是正方形
    if w != h:
        raise ValueError("图片必须是正方形")

    # 定义区域颜色
    colors = [
        (255, 0, 0),  # 红色
        (0, 255, 0),  # 绿色
        (0, 0, 255),  # 蓝色
        (255, 255, 0),  # 黄色
        (255, 165, 0),  # 橙色
        (128, 0, 128),  # 紫色
        (0, 255, 255),  # 青色
        (255, 192, 203)  # 粉色
    ]

    # 创建一个绘图对象
    draw = ImageDraw.Draw(img)

    # 中心点
    cx, cy = w // 2, h // 2

    # 坐标片段
    sections = [
        (0, 0, cx, cy),  # 左上
        (cx, 0, w, cy),  # 右上
        (0, cy, cx, h),  # 左下
        (cx, cy, w, h),  # 右下
        (w//4, 0, (3*w)//4, h//2),  # 垂直中间
        (0, h//4, w//2, (3*h)//4),  # 水平中间左
        (w//2, h//4, w, (3*h)//4),  # 水平中间右
        (w//4, h//2, (3*w)//4, h)   # 水平中间下
    ]

    # 绘制矩形并填充颜色
    for index, (x1, y1, x2, y2) in enumerate(sections):
        draw.rectangle([x1, y1, x2, y2], outline=colors[index], width=3)
        draw.polygon([x1, y1, x2, y1, x2, y2, x1, y2], fill=colors[index] + (100,))

    # 显示图片
    img.show()

# 示例使用
image_path = "path/to/your/image.jpg"  # 替换为你的图片路径
divide_and_color_image(image_path)
