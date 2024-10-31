def is_point_in_square(px, py, vertices):
    # 将顶点转换为向量
    v0 = np.array(vertices[0])
    v1 = np.array(vertices[1])
    v2 = np.array(vertices[2])
    v3 = np.array(vertices[3])
    
    # 计算正方形的两个边向量
    edge1 = v1 - v0
    edge2 = v3 - v0
    
    # 计算点相对于第一个顶点的向量
    point_vector = np.array([px, py]) - v0
    
    # 计算点在两个边向量上的投影
    dot1 = np.dot(point_vector, edge1) / np.dot(edge1, edge1)
    dot2 = np.dot(point_vector, edge2) / np.dot(edge2, edge2)
    
    # 检查点是否在正方形内
    return 0 <= dot1 <= 1 and 0 <= dot2 <= 1

def get_all_points_in_rotated_square(vertices):
    # 找到x和y的边界
    x_coords = [vertex[0] for vertex in vertices]
    y_coords = [vertex[1] for vertex in vertices]
    
    min_x = int(min(x_coords))
    max_x = int(max(x_coords))
    min_y = int(min(y_coords))
    max_y = int(max(y_coords))
    
    # 检查每个点是否在正方形内
    points = []
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if is_point_in_square(x, y, vertices):
                points.append((x, y))
    
    return points
