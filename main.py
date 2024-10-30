from PIL import Image, ImageDraw

def draw_square(image_path, point, size):
    # 打开图像
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    
    # 计算正方形的位置
    left = point[0]
    top = point[1] - size // 2
    right = left + size
    bottom = top + size
    
    # 绘制正方形
    draw.rectangle([left, top, right, bottom], outline="green", fill="green")
    
    # 显示或保存结果图像
    img.show()
    # img.save('result.png')  # 如果您想保存修改后的图像

# 调用函数
draw_square('your_image_path_here.jpg', (57, 51), 5)
