import torch
import torch.nn as nn
import torch.nn.functional as F

class FeatureExtractor(nn.Module):
    def __init__(self, num_classes=3):
        super(FeatureExtractor, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )

        self.position_embed = nn.Conv2d(2, 128, kernel_size=1)  # 用于生成位置编码

        self.decoder = nn.Sequential(
            nn.Conv2d(256, 64, kernel_size=3, padding=1),  # 注意通道数增加
            nn.ReLU(inplace=True),
            nn.Conv2d(64, 1, kernel_size=3, padding=1),
            nn.Upsample(scale_factor=4, mode='bilinear', align_corners=True)
        )

    def generate_position_tensor(self, height, width):
        y_embed = torch.linspace(0, 1, height).unsqueeze(1).repeat(1, width).unsqueeze(0)
        x_embed = torch.linspace(0, 1, width).unsqueeze(0).repeat(height, 1).unsqueeze(0)
        return torch.cat([y_embed, x_embed], dim=0).unsqueeze(0)  # shape [1, 2, height, width]

    def forward(self, x):
        position_tensor = self.generate_position_tensor(x.size(2), x.size(3)).to(x.device)
        position_embedding = self.position_embed(position_tensor)
        
        x = self.encoder(x)
        combined_features = torch.cat([x, position_embedding.repeat(x.size(0), 1, 1, 1)], dim=1)
        x = self.decoder(combined_features)
        return x
