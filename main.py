import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import numpy as np
from torch.autograd import Variable
from my_data import Data  # 假设Data类是在一个名为my_data的脚本中定义

class FeatureExtractor(nn.Module):
    def __init__(self):
        super(FeatureExtractor, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.relu1 = nn.ReLU()
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=1, kernel_size=3, stride=1, padding=1)
        self.relu2 = nn.ReLU()

    def forward(self, x):
        x = self.relu1(self.conv1(x))
        x = self.relu2(self.conv2(x))
        return x

def train_classifer(model, checkpoints_path):
    data_root = r'E:\\BDCN-master\\testdata'
    data_lst = 'train_pair.lst'
    mean_bgr = np.array([104.00699, 116.66877, 122.67892])
    yita = 0.4
    crop_size = None

    train_img = Data(data_root, data_lst, yita, mean_bgr=mean_bgr, crop_size=crop_size)
    trainloader = torch.utils.data.DataLoader(train_img, batch_size=1, shuffle=True, num_workers=5)

    cur = 0
    data_iter = iter(trainloader)
    iter_per_epoch = len(trainloader)
    beta = 0.1

    base_model = model
    state = torch.load(checkpoints_path, map_location='cpu')
    base_model.load_state_dict(state)

    for param in base_model.parameters():
        param.requires_grad = False

    feature_extractor = FeatureExtractor()
    optimizer = torch.optim.SGD(feature_extractor.parameters(), momentum=0.9, lr=0.001, weight_decay=0.001)
    feature_extractor.train()

    if torch.cuda.is_available():
        base_model.cuda()
        feature_extractor.cuda()

    for epoch in range(50):
        batch_loss = 0
        for i in range(iter_per_epoch):
            if cur == iter_per_epoch:
                cur = 0
                data_iter = iter(trainloader)
            
            images, labels = next(data_iter)
            if torch.cuda.is_available():
                images, labels = images.cuda(), labels.cuda()
            
            images, labels = Variable(images), Variable(labels)
            with torch.no_grad():
                features = base_model(images)
                fused_map = features[-1]
                out = torch.sigmoid(fused_map).cpu().data.numpy()
            
            feature_map = feature_extractor(fused_map)
            map = torch.sigmoid(feature_map)
            
            labels = torch.where(labels >= yita, torch.tensor(1.0, device=labels.device), torch.tensor(0.0, device=labels.device))
            
            fused_bin_map = torch.where(out >= yita, torch.tensor(1.0), torch.tensor(0.0))
            new_label = torch.where(labels == 1, torch.tensor(1.0), torch.where(fused_bin_map == 1, torch.tensor(0.0), torch.tensor(0.5)))
            
            num_positive_true = torch.sum(new_label == 1).float()
            num_negative_true = torch.sum(new_label == 0).float()
            mask = torch.where(new_label == 1, 1.0 * num_negative_true / (num_negative_true + num_positive_true), 
                                  torch.where(new_label == 0, beta * num_positive_true / (num_negative_true + num_positive_true), torch.tensor(0.0)))
            
            loss = F.binary_cross_entropy(map, labels, weight=mask, reduction='sum')
            loss.backward()
            batch_loss += loss.item()
            cur += 1
        optimizer.step()
        print(f'Epoch [{epoch + 1}/50], Loss: {loss.item():.4f}')
