self.encoder = nn.Sequential(
       nn.Conv2d(in_channels=5, out_channels=64, kernel_size=3, padding=1),
       nn.ReLU(inplace=True),
       nn.Dropout(0.5),  # Dropout layer
       nn.MaxPool2d(kernel_size=2, stride=2),
       nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1),
       nn.ReLU(inplace=True),
       nn.Dropout(0.5),  # Dropout layer
       nn.MaxPool2d(kernel_size=2, stride=2)
   )
