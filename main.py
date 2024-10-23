def find_y_value(d, thresh):
    # 把强度值除以5
    d = {k: v / 5 for k, v in d.items()}
    
    # 按y的值从小到大排序
    sorted_items = sorted(d.items())
    
    # 遍历所有y的值，找到第一个符合条件的
    for y, intensity in sorted_items:
        if intensity > thresh:
            return y
    
    # 如果没有找到符合条件的值，返回None
    return None


# 示例字典
d = {
    58: 326.8625193847768,
    59: 88.41092178101273,
    60: 511.08902684585762,
    61: 624.0675913836851,
    62: 1831.24699056712966,
    63: 1961.3456440528098,
    64: 817.7538061704564,
    65: 213.56610930077673,
    66: 582.4233078671347,
    67: 9422.5185305268745,
    68: 1038.215331300595
}

# 设定阈值
thresh = 200.0

# 调用函数
result = find_y_value(d, thresh)
print(result)
