# 找到 f1 最大的那一组
max_f1_group = max(result_dict.values(), key=lambda x: x['f1'])

print(max_f1_group)
