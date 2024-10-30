def average_of_points(points, calculate):
    total = 0
    count = len(points)
    
    for x, y in points:
        total += calculate(x, y)
    
    return total / count if count > 0 else None

# 示例
points = [(1, 2), (3, 4), (5, 6)]

# 这里定义一个简单的计算函数作为例子
def calculate(x, y):
    return x + y

average = average_of_points(points, calculate)
print("平均值:", average)
