import torch
from torchvision import models
from torchvision.models.feature_extraction import create_feature_extractor

# 加载预训练的Wide ResNet模型
model = models.wide_resnet101_2(pretrained=True)
print(model)

# 指定你感兴趣的层
return_nodes = {'layer1': 'layer1_output'}

# 创建特征提取器
feature_extractor = create_feature_extractor(model, return_nodes)

# 输入数据，进行前向传播
input_data = torch.rand(1, 3, 512, 512)
features = feature_extractor(input_data)

# 获取特定层的输出
layer_output = features['layer1_output']
print(layer_output.shape)
