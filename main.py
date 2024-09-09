self.encoder = nn.Sequential(
    nn.Conv2d(in_channels=5, out_channels=64, kernel_size=3, padding=1),
    nn.BatchNorm2d(64),
    nn.ReLU(inplace=True),
    nn.Dropout(0.5),
    nn.MaxPool2d(kernel_size=2, stride=2),
    nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1),
    nn.BatchNorm2d(128),
    nn.ReLU(inplace=True),
    nn.Dropout(0.5),
    nn.MaxPool2d(kernel_size=2, stride=2)
)

self.decoder = nn.Sequential(
    nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, padding=1),
    nn.BatchNorm2d(128),
    nn.ReLU(inplace=True),
    nn.Conv2d(in_channels=128, out_channels=64, kernel_size=3, padding=1),
    nn.BatchNorm2d(64),
    nn.ReLU(inplace=True),
    nn.Conv2d(in_channels=64, out_channels=1, kernel_size=3, padding=1),
    nn.Upsample(scale_factor=4, mode='bilinear', align_corners=True)
)
