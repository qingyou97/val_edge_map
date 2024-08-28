import torch
import torch.nn as nn
import torch.optim as optim

# 定义一个简单的CNN
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, padding=1)
        self.relu1 = nn.ReLU()
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.relu2 = nn.ReLU()
        self.fc = nn.Linear(32*8*8, 10)  # 假设输入图片大小为8x8，最后输出10类

    def forward(self, x):
        x = self.relu1(self.conv1(x))
        x = self.relu2(self.conv2(x))
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x

# 构造分类器和损失函数、优化器
model = SimpleCNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 假设我们有一个8x8的随机图像和对应的标签
input_image = torch.randn(1, 1, 8, 8)
label = torch.tensor([3])  # 随机的示例标签，假设一共有10个类

# 训练模型
for epoch in range(10):  # 训练10个epoch
    optimizer.zero_grad()
    outputs = model(input_image)
    loss = criterion(outputs, label)
    loss.backward()
    optimizer.step()

    print(f'Epoch {epoch + 1}, Loss: {loss.item():.4f}')
