import matplotlib.pyplot as plt
from PIL import Image

def mark_top_point(image_path, coordinates):
    # 加载图像
    image = Image.open(image_path)
    
    # 找到最小的y值，也就是最靠上的点
    top_y = min(coordinates, key=lambda point: (point[1], -point[0]))
    # 这个点的x坐标
    top_x = top_y[0]
    
    # 标注这个点在图像上的位置
    plt.imshow(image)
    plt.scatter(top_x, top_y[1], color='green', marker='o')
    plt.title(f"Top point at x={top_x}, y={top_y[1]}")
    
    # 显示图像
    plt.show()
    
    # 返回x值
    return top_x

# 示例图像路径与坐标
image_path = 'path/to/your/image.png'  # 替换为你的图像路径
coordinates = [(23, 45), (50, 10), (120, 10), (150, 20)]  # 示例坐标

# 调用函数并获取x坐标
x = mark_top_point(image_path, coordinates)
print("Top point's x coordinate:", x)
