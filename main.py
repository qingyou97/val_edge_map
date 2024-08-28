import torch
import torch.nn as nn
import torch.optim as optim


class FeatureExtractor(nn.Module):
    def __init__(self, num_classes):
        super(FeatureExtractor, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.relu1 = nn.ReLU()

        self.conv2 = nn.Conv2d(in_channels=64, out_channels=num_classes, kernel_size=3, stride=1, padding=1)


        # nn.init.constant_(self.conv1.weight, 10)
        # nn.init.constant_(self.conv1.bias, 1)
        #
        # nn.init.constant_(self.conv2.weight, 15)
        # nn.init.constant_(self.conv2.bias, 4)

    def forward(self, x):
        x = self.relu1(self.conv1(x))
        x = self.conv2(x)
        # print(x.shape)
        return x
