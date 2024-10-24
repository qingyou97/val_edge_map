import numpy as np
import cv2

def find_two_circles(path):
    #读取图像
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (224, 224))
    result = []

    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 创建两个空白图像来绘制两个圆环
    output_image1 = np.zeros_like(image)
    
    ellipses = []
    for contour in contours:
        # 拟合椭圆轮廓，确保轮廓具有足够的点
        if len(contour) >= 5:
            ellipse = cv2.fitEllipse(contour)
            ellipses.append(ellipse)

    if len(ellipses) >= 4:
        # 按面积排序，确保第一个和第二个是一个圆环的内外轮廓，第三个和第四个是另一个圆环的内外轮廓
        ellipses = sorted(ellipses, key=lambda e: e[1][0] * e[1][1], reverse=True)

        def make_circle(ellipse):
            center, axes, angle = ellipse
            max_radius = max(axes)
            return (center, (max_radius, max_radius), angle)

        def adjust_inner_circle(outer, inner):
            outer_center, outer_axes, outer_angle = outer
            inner_center, inner_axes, inner_angle = inner
            # 调整内圆心到外圆心
            inner_center = outer_center
            # 如果内圆需要调整
            if inner_axes[0] > outer_axes[0]:
                inner_axes = (outer_axes[0] - 10, outer_axes[0] - 10)  # 这里减去10是为了确保内圆小于外圆
            elif inner_axes[0] < outer_axes[0]:
                inner_axes = (outer_axes[0] - 10, outer_axes[0] - 10)  # 这里减去10是为了确保内圆小于外圆
            return (inner_center, inner_axes, inner_angle)

        ellipses[0] = make_circle(ellipses[0])
        ellipses[1] = adjust_inner_circle(ellipses[0], make_circle(ellipses[1]))
        ellipses[2] = make_circle(ellipses[2])
        ellipses[3] = adjust_inner_circle(ellipses[2], make_circle(ellipses[3]))

    return ellipses, output_image1

def draw_ellipses(image, ellipses):
    for center, axes, angle in ellipses:
        cv2.ellipse(image, (int(center[0]), int(center[1])), (int(axes[0]), int(axes[1])), angle, 0, 360, (255, 255, 255), 2)

def rgba_points(image, color=[253, 231, 36, 255]):
    mask = cv2.inRange(image, np.array(color), np.array(color))
    coordinates = cv2.findNonZero(mask)
    return coordinates

def is_point_in_ellipse(point, ellipse):
    center, axes, angle = ellipse
    axes = (axes[0] / 2, axes[1] / 2)
    px, py = point[0], point[1]
    cos_angle = np.cos(np.radians(angle))
    sin_angle = np.sin(np.radians(angle))
    dx = px - center[0]
    dy = py - center[1]
    x = cos_angle * dx + sin_angle * dy
    y = -sin_angle * dx + cos_angle * dy
    return (x / axes[0]) ** 2 + (y / axes[1]) ** 2 <= 1

def adjust_ellipses(ellipses, points):
    total_points = len(points)
    while True:
        covered_points = 0
        for point in points:
            for ellipse in ellipses:
                if is_point_in_ellipse(point[0], ellipse):
                    covered_points += 1
                    break
        coverage = covered_points / total_points
        if coverage >= 0.95:
            break
        
        for i in range(len(ellipses)):
            center, axes, angle = ellipses[i]
            axes = (axes[0] * 1.01, axes[1] * 1.01)
            ellipses[i] = (center, axes, angle)
            
    return ellipses

# 你的图像路径
image_path1 = 'path_to_your_first_image.jpg'
image_path2 = 'path_to_your_second_image.png'

ellipses, output_image1 = find_two_circles(image_path1)

# 读取第二张图像
second_image = cv2.imread(image_path2, cv2.IMREAD_UNCHANGED)
selected_points = rgba_points(second_image)

# 调整圆环以覆盖选定点
adjusted_ellipses = adjust_ellipses(ellipses, selected_points)

# 绘制调整后的圆环
output_image_with_circles = cv2.cvtColor(output_image1, cv2.COLOR_GRAY2BGR)
draw_ellipses(output_image_with_circles, adjusted_ellipses)

# 保存输出结果
cv2.imwrite('output_image_with_circles.jpg', output_image_with_circles)
