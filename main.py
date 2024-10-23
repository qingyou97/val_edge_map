def count_intensity_intervals(data, interval=50):
    """
    计算并统计每个强度值区间内的点数。
    
    :param data: list of lists, 形如 [[(x, y), intensity], ...]
    :param interval: int, 区间大小，默认为50
    :return: dict, 形如 {区间: 点数}
    """
    if not data:
        return {}

    # 初始化区间统计字典
    interval_counts = {}

    for item in data:
        _, intensity = item
        # 计算强度值所在的区间
        interval_key = (int(intensity) // interval) * interval
        if interval_key not in interval_counts:
            interval_counts[interval_key] = 0
        interval_counts[interval_key] += 1

    return interval_counts

# 示例用法
data = [[(220, 116), 284.0633732109791], 
        [(215, 122), 180.0567890], 
        [(210, 118), 300.56473820],
        [(225, 120), 150.1234567],
        [(230, 125), 200.9876543],
        [(235, 130), 100.4567890],
        [(240, 135), 250.1234567]]

interval_counts = count_intensity_intervals(data)
for interval, count in sorted(interval_counts.items()):
    print(f"区间 {interval}-{interval + 49}: {count} 个点")
