def filter_and_sort_intensities(data, thresh):
    # 筛选出强度值大于thresh的项
    filtered_data = {y: intensity for y, intensity in data.items() if intensity > thresh}
    
    # 按照y值排序
    sorted_filtered_data = dict(sorted(filtered_data.items()))
    
    return sorted_filtered_data

# 示例字典
data = {54: 449.3646893061633, 55: 1297.34465165651155, 56: 1805.3129851341728, 57:1154.4329935468359, 
           58: 326.8625193847768, 59: 88.410921781012733, 60:51.08902684585762, 61: 624.0675913836851, 
           62: 1831.2469056712966, 63: 1961.3456440528098, 64: 817.7538061704564, 65:213.56610930077673, 
           66: 582.4233078671347, 67: 942.5185305268745, 68: 1038.215331300595, 69:1127.5610874995525, 
           70: 801.99001550009673, 71: 261.0890344860568, 72: 101.20416736553082}

# 示例阈值
thresh = 800

result = filter_and_sort_intensities(data, thresh)
print(result)
