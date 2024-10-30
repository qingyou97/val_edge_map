from PIL import Image, ImageDraw

def draw_square_and_points(image_path, square_center, size, points_list):
    # 打开图像
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    
    # 计算正方形的位置
    left = square_center[0]
    top = square_center[1] - size // 2
    right = left + size
    bottom = top + size
    
    # 绘制正方形
    draw.rectangle([left, top, right, bottom], outline="green", fill=None)
    
    # 找出在正方形内的点
    points_in_square = [
        (x, y) for (x, y) in points_list
        if left <= x < right and top <= y < bottom
    ]
    
    # 绘制在正方形内的点
    for point in points_in_square:
        draw.ellipse((point[0] - 1, point[1] - 1, point[0] + 1, point[1] + 1), fill="red")
    
    # 显示图像
    img.show()
    
    return points_in_square

# 示例使用
image_path = 'your_image_path_here.jpg'
square_center = (57, 51)
size = 5
points_list = [(2, 3), (4, 5), (57, 50), (58, 51), (59, 52)]
result = draw_square_and_points(image_path, square_center, size, points_list)
print(result)
