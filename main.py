def distance_point_to_circle(px, py, cx, cy, r):
    # 计算点 (px, py) 到圆心 (cx, cy) 的欧氏距离
    center_distance = math.sqrt((px - cx) ** 2 + (py - cy) ** 2)
    # 垂直距离是欧氏距离减去圆的半径
    return abs(center_distance - r)

def find_nearest_circle(px, py, circles):
    # 储存最小距离和最近圆的索引
    min_distance = float('inf')
    nearest_circle_idx = -1
    for idx, (cx, cy, r) in enumerate(circles):
        dist = distance_point_to_circle(px, py, cx, cy, r)
        if dist < min_distance:
            min_distance = dist
            nearest_circle_idx = idx
    return nearest_circle_idx, min_distance

def plot_circles_and_point(px, py, circles, nearest_circle_idx, filename='output.png'):
    # 创建一个224x224的白色图像
    img = np.ones((224, 224, 3), dtype=np.uint8) * 255
    
    for (cx, cy, r) in circles:
        # 画圆
        cv2.circle(img, (cx, cy), r, (0, 0, 0), 1)
    
    # 标记给定的点
    cv2.circle(img, (px, py), 3, (255, 0, 0), -1) # 使用蓝色点标记
    
    # 画出垂直距离线
    nearest_circle = circles[nearest_circle_idx]
    cx, cy, r = nearest_circle
    vector = [(px - cx, py - cy) for _ in range(1)]
    unit_vector = (vector[0][0] / np.linalg.norm(vector), vector[0][1] / np.linalg.norm(vector))
    edge_point_x = int(cx + unit_vector[0] * r)
    edge_point_y = int(cy + unit_vector[1] * r)
    cv2.line(img, (px, py), (edge_point_x, edge_point_y), (0, 0, 255), 1) # 红线作为垂直距离
    
    # 保存图像
    cv2.imwrite(filename, img)
    
    # 显示图像
    cv2.imshow('Circles and Point', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def main(px, py, circles):
    nearest_circle_idx, min_distance = find_nearest_circle(px, py, circles)
    print(f"点到最近圆的垂直距离为 {min_distance:.2f} 像素")
    print(f"最近的圆是: 圆心 ({circles[nearest_circle_idx][0]}, {circles[nearest_circle_idx][1]}), 半径 {circles[nearest_circle_idx][2]}")
    plot_circles_and_point(px, py, circles, nearest_circle_idx)
    return min_distance

# 输入给定的点和四个圆的数据
px = 100  # 给出的点的x坐标
py = 150  # 给出的点的y坐标
circles = [(50, 50, 20), (160, 160, 30), (80, 180, 25), (200, 200, 15)]

# 调用主函数并获取距离
distance = main(px, py, circles)
print(f"返回的距离: {distance:.2f} 像素")
