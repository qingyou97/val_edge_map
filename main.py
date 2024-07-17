import torch

# 加载模型权重
model_path = 'your_model_path.pth'
model = torch.load(model_path, map_location=torch.device('cpu'))

# 打印模型的层和参数名字
for name, param in model.items():
    print(f"Layer: {name} | Size: {param.size()}")
```

注意：上述代码假设模型保存的字典状态。如果模型是通过 `torch.save(model.state_dict(), path)` 保存的，可以使用 `model.load_state_dict()` 的 `state_dict` 替代 `model`。

```python
# 加载 model.state_dict()
state_dict = torch.load(model_path, map_location=torch.device('cpu'))

# 输出每个参数的名字和大小
for name, param in state_dict.items():
    print(f"Parameter: {name} | Size: {param.size()}")
