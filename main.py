class FeatureExtractor(nn.Module):
    def __init__(self, num_classes):
        super(FeatureExtractor, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.relu1 = nn.ReLU()
        self.bn1 = nn.BatchNorm2d(64)
        self.conv2 = nn.Conv2d(in_channels=64, out_channels=num_classes, kernel_size=3, stride=1, padding=1)
        self.relu2 = nn.ReLU()
        self.bn2 = nn.BatchNorm2d(num_classes)
      
    def forward(self, x):
        x = self.relu1(self.bn1(self.conv1(x)))
        x = self.conv2(x)
        return x
