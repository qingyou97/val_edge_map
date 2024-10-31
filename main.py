def sort_dict_by_value(data):
    # 按照值从大到小排序，并转换为列表
    sorted_list = sorted(data.items(), key=lambda item: item[1], reverse=True)
    return sorted_list

# 示例使用
data = {1: 11, 2: 23, 3: 45}
sorted_list = sort_dict_by_value(data)
print(sorted_list)
