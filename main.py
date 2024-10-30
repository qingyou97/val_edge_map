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
# draw_square_and_points_on_image(img, rotated_square, points_inside)import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_square_and_points(rotated_square, points_inside):
    # 创建一个新的图形
    fig, ax = plt.subplots()

    # 创建一个Polygon对象，并添加到图形中
    square = patches.Polygon(rotated_square, closed=True, fill=False, edgecolor='green')
    ax.add_patch(square)
    
    # 在图中绘制点
    x_vals, y_vals = zip(*points_inside)
    ax.scatter(x_vals, y_vals, color='red', zorder=5)

    # 设置轴的范围，让图形更易于查看
    all_x = [point[0] for point in rotated_square] + x_vals
    all_y = [point[1] for point in rotated_square] + y_vals
    padding = 5
    ax.set_xlim(min(all_x) - padding, max(all_x) + padding)
    ax.set_ylim(min(all_y) - padding, max(all_y) + padding)
    
    # 设置等比例显示
    ax.set_aspect('equal', adjustable='box')

    # 显示图像
    plt.show()

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

plot_square_and_points(rotated_square, points_inside)
