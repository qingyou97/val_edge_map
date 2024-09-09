class FeatureExtractorWithPosition(nn.Module):
    def __init__(self, num_classes=3):
        super(FeatureExtractorWithPosition, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(5, 64, kernel_size=3, padding=1),  # 调整输入通道数量为5：3（颜色通道）+ 2（位置通道）
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )

        self.decoder = nn.Sequential(
            nn.Conv2d(128, 64, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(64, 1, kernel_size=3, padding=1),
            nn.Upsample(scale_factor=4, mode='bilinear', align_corners=True)
        )

    def forward(self, x):
        batch_size, _, h, w = x.shape
        pos_y, pos_x = torch.meshgrid(torch.linspace(0, 1, h), torch.linspace(0, 1, w), indexing='ij')
        pos_x = pos_x.unsqueeze(0).unsqueeze(0).expand(batch_size, -1, -1, -1)  # (B, 1, H, W)
        pos_y = pos_y.unsqueeze(0).unsqueeze(0).expand(batch_size, -1, -1, -1)  # (B, 1, H, W)
        position_encoding = torch.cat([pos_x, pos_y], dim=1).to(x.device)  # (B, 2, H, W)
        x = torch.cat([x, position_encoding], dim=1)  # (B, 5, H, W)

        x = self.encoder(x)
        x = self.decoder(x)
        return x
