import torch
import torch.nn as nn
import torch.nn.functional as F

class SimpleEdgeClassifier(nn.Module):
    def __init__(self, num_classes):
        super(SimpleEdgeClassifier, self).__init__()
        # 第一层卷积
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1)
        self.batch_norm1 = nn.BatchNorm2d(16)
        
        # 第二层卷积
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        self.batch_norm2 = nn.BatchNorm2d(32)

        # 第三层卷积
        self.conv3 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.batch_norm3 = nn.BatchNorm2d(64)
        
        # 平均值池化层
        self.pool = nn.AdaptiveAvgPool2d((1, 1))
        
        # 全连接层
        self.fc = nn.Linear(64, num_classes)

    def forward(self, x):
        x = F.relu(self.batch_norm1(self.conv1(x)))
        x = F.max_pool2d(x, 2)
        
        x = F.relu(self.batch_norm2(self.conv2(x)))
        x = F.max_pool2d(x, 2)

        x = F.relu(self.batch_norm3(self.conv3(x)))
        x = F.max_pool2d(x, 2)

        # 平均池化，展平，用全连接层输出
        x = self.pool(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x
