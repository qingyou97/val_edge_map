# 去掉前缀 'features.'
new_state_dict = {}
for k in state_dict:
    new_key = k.replace('features.', '')  # 去掉前缀
    new_state_dict[new_key] = state_dict[k]

# 加载修改后的 state_dict
model_class.load_state_dict(new_state_dict)
