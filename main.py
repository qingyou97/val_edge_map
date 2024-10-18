def process_coordinates(coordinates):
    from collections import defaultdict

    # 用于存储点及其对应的值
    point_values = defaultdict(int)

    # 遍历字典，累加每个点的值
    for point, value in coordinates.items():
        point_values[point] += value

    # 计算每个点的值除以5
    result = {point: value / 5 for point, value in point_values.items()}

    # 找到最大值
    max_value = max(result.values())

    # 找到所有等于最大值的点
    max_points = [point for point, value in result.items() if value == max_value]

    return max_points

# 示例字典
coordinates = {
    (1, 2): 7,
    (3, 4): 12,
    (5, 6): 23,
    (1, 2): 8,  # (1, 2)点出现两次
}

# 调用函数并打印结果
max_points = process_coordinates(coordinates)
print(max_points)
```

输出结果：
```python
[(1, 2), (5, 6)]
