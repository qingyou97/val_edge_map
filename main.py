class CustomModel(nn.Module):
    def __init__(self, bdcn_model):
        super(CustomModel, self).__init__()
        self.bdcn_model = bdcn_model
        # 定义你自己的分类器，这里是一个简单的全连接层示例
        self.classifier = nn.Sequential(
            nn.Linear(bdcn_model.output_feature_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 10)  # 假设你有10个类别
        )

    def forward(self, x):
        # pass inputs through the entire bdcn model
        out = self.bdcn_model(x)
        # assuming `out[-1]` is the fused output from BDCN's forward method
        fused_output = out[-1].view(out[-1].size(0), -1)
        # pass the fused output through the classifier
        classification = self.classifier(fused_output)
        return out, classification
