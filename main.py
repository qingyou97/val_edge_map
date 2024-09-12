import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F


def crop(data1, data2, crop_h, crop_w):
    _, _, h1, w1 = data1.size()
    _, _, h2, w2 = data2.size()
    # _, _, h2, w2 = _, _, 512, 512
    assert (h2 <= h1 and w2 <= w1)
    data = data1[:, :, crop_h:crop_h + h2, crop_w:crop_w + w2]
    return data


# model for middle output sum3
class FeatureExtractor(nn.Module):
    def __init__(self, num_classes):
        super(FeatureExtractor, self).__init__()

        self.conv1 = nn.Conv2d(1024, 512, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(1024, 512, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(768, 384, kernel_size=3, padding=1)
        self.conv4 = nn.Conv2d(384, 1, kernel_size=3, padding=1)

        self.bn1 = nn.BatchNorm2d(512)
        self.bn2 = nn.BatchNorm2d(512)
        self.bn3 = nn.BatchNorm2d(384)
        self.bn4 = nn.BatchNorm2d(512)

    def forward(self, middle_output_list):
        map1, map2, map3 = middle_output_list
        map3 = self.conv1(map3)
        map3 = self.bn1(map3)
        map3 = F.relu(map3)
        # print(f'map3:{map3.shape}')

        map3 = F.interpolate(map3, size=(64, 64), mode='nearest')
        map3 = torch.cat((map3, map2), dim=1)

        map3 = self.conv2(map3)
        map3 = self.bn2(map3)
        map3 = F.relu(map3)

        map3 = F.interpolate(map3, size=(128, 128), mode='nearest')
        map3 = torch.cat((map3, map1), dim=1)

        map3 =  self.conv3(map3)
        map3 = self.bn3(map3)
        map3 = F.relu(map3)

        out = F.interpolate(map3, size=(512, 512), mode='nearest')
        out = self.conv4(out)
        # print(out.shape)

        return out



if __name__ == '__main__':
    model = FeatureExtractor(3)
    map =[]
    map3 = torch.rand([1, 1024, 32, 32])
    map2 = torch.rand([1, 512, 64, 64])
    map1 = torch.rand([1, 256, 128, 128])

    map3 = torch.autograd.Variable(map3)
    map1 = torch.autograd.Variable(map1)
    map2 = torch.autograd.Variable(map2)
    map.append(map1)

    map.append(map2)
    map.append(map3)

    model(map)


    
