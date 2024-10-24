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
