def process_points(points, circles): 
    def cal_neareest_circle_idx(px, py, circles):
        # This is a placeholder. 
        # Replace it with the actual function implementation.
        distance = None
        position = (px, py)
        nearest_circle_idx = None
        return distance, position, nearest_circle_idx
    
    result_list = []
    max_distance = float('-inf')
    max_distance_point = {}
    
    for point in points:
        px, py = point
        distance, position, nearest_circle_idx = cal_neareest_circle_idx(px, py, circles)
        result = {
            "point": point,
            "distance": distance,
            "position": position,
            "nearest_circle_idx": nearest_circle_idx
        }
        result_list.append(result)
        
        if distance > max_distance:
            max_distance = distance
            max_distance_point = result
    
    return result_list, max_distance_point

# 示例调用
points = [(1,1),(1,2),(1,3)]
circles = [/* 圆的参数 */]
result_list, max_distance_point = process_points(points, circles)
print("返回的结果列表：", result_list)
print("最大distance的点和相关信息：", max_distance_point)
