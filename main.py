from PIL import Image, ImageDraw

def draw_square_and_points_on_image(img, rotated_square, points_inside):
    # 创建一个Draw对象
    draw = ImageDraw.Draw(img)

    # 绘制绿色正方形
    draw.polygon(rotated_square, outline='green')

    # 绘制红色点
    for point in points_inside:
        # 这里假设点的大小为3x3像素
        x, y = point
        draw.ellipse((x-1, y-1, x+1, y+1), fill='red')

    # 显示图像
    img.show()

# 假设你已经有一个PIL图像对象img
# img = Image.open('your_image_path.jpg')

# 样例数据调用
rotated_square = [
    (55.81844513364193, 46.141612603158784),
    (58.18155486635807, 55.858387396841216),
    (67.8983296600405, 53.49527766412508),
    (65.53521992732436, 43.778502870442644)
]

points_inside = [
    (63, 48), (64, 48), (65, 48), (66, 48), 
    (59, 49), (60, 449), (61, 49), (62, 49), (63, 49)
]

# 调用函数
# draw_square_and_points_on_image(img, rotated_square, points_inside)
