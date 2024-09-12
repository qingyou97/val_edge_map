import numpy as np
import torch
import torch.optim as optim
import torch.nn as nn
from torch.autograd import Variable
from torch.nn import functional as F
import time
import re
import os
import sys
import cv2
import bdcn
from datasets.dataset import Data
import argparse
import cfg
from matplotlib import pyplot as plt
import os
import os.path as osp
from scipy.io import savemat


def make_dir(data_dir):
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)


def test(bdcn_model, class_model, data_root, res_dir):
    from torchvision import models
    # 加载 Wide ResNet-101-2 预训练模型
    wide_model = models.wide_resnet101_2()

    mean_bgr = np.array([104.00699, 116.66877, 122.67892])

    test_root = data_root

    test_lst = os.listdir(test_root)

    save_dir = res_dir
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    bdcn_model.eval()
    class_model.eval()
    wide_model.eval()

    # 定义一个字典来存储特定层的输出
    outputs = {}

    # 定义一个 hook 函数
    def hook_fn(module, input, output):
        outputs[module] = output

    # 注册 hook 到你感兴趣的层
    layers_to_hook = [wide_model.layer1, wide_model.layer2, wide_model.layer3, wide_model.layer4]
    hooks = []
    for layer in layers_to_hook:
        hook = layer.register_forward_hook(hook_fn)
        hooks.append(hook)

    all_t = 0

    for nm in test_lst:
        data = cv2.imread(test_root + '/' + nm)

        print(f'Processing data: {nm}')

        data = np.array(data, np.float32)
        data -= mean_bgr
        data = data.transpose((2, 0, 1))
        data = torch.from_numpy(data).float().unsqueeze(0)

        data = Variable(data)

        t1 = time.time()
        out = bdcn_model(data)

        if '/' in nm:
            nm = nm.split('/')[-1]

        fused_map = out[-1].cpu().data

        wide_model(data)
        wide_maps = []
        for layer, output in outputs.items():
            # print(f"Output of layer shape: {output.shape}")
            wide_maps.append(output)

        wide_map_list = []
        wide1 = wide_maps[0]
        wide2 = wide_maps[1]
        wide3 = wide_maps[2]

        wide_map_list.append(Variable(wide1))
        wide_map_list.append(Variable(wide2))
        wide_map_list.append(Variable(wide3))


        bdcn_map_sigmid = F.sigmoid(fused_map).cpu().data.numpy()
        bdcn_save_out = bdcn_map_sigmid[0, 0, :, :]

        feature_map = class_model(wide_map_list)

        class_map = F.sigmoid(feature_map).cpu().data.numpy()[0, 0, :, :]

        # 保存原模型的fused map
        if not os.path.exists(os.path.join(save_dir, 'fuse')):
            os.mkdir(os.path.join(save_dir, 'fuse'))
        cv2.imwrite(os.path.join(save_dir, 'fuse/%s.png' % nm.split('/')[-1].split('.')[0]),
                    255 - 255 * bdcn_save_out[-1])

        # 保存经过分类之后的模型
        if not os.path.exists(os.path.join(save_dir, 'class_1')):
            os.mkdir(os.path.join(save_dir, 'class_1'))
        if not os.path.exists(os.path.join(save_dir, 'class_0')):
            os.mkdir(os.path.join(save_dir, 'class_0'))
        if not os.path.exists(os.path.join(save_dir, 'class_2')):
            os.mkdir(os.path.join(save_dir, 'class_2'))


        cv2.imwrite(os.path.join(save_dir, 'class_1/%s.png' % nm.split('/')[-1].split('.')[0]), 255-255 * class_map)

        all_t += time.time() - t1

    # print('infer time', all_t)
    # print('Overall Time use: ', time.time() - start_time)
    # print('len test_list', len(test_lst))
    # print('fps', len(test_lst) / all_t)


def main():

    from classifier_wider import FeatureExtractor
    bdcn_ckpt_path = r'E:\BDCN-master\BDCNmodel\bdcn_pretrained_on_bsds500.pth'

    # 加载原模型
    bdcn_model = bdcn.BDCN()
    bdcn_model.load_state_dict(torch.load(bdcn_ckpt_path, map_location=torch.device('cpu')))


    # 加载分类模型
    num_classes = 3
    class_model = FeatureExtractor(num_classes)

    folder = '3class_wide'

    data_root = rf'E:\BDCN-master\testdata\casting'

    epoch_path = rf'E:\BDCN-master\checkpoints\{folder}'
    ck_epoch_list = os.listdir(epoch_path)
    # for epoch in ck_epoch_list:
    for epoch in range(1, 1000, 10):
        class_ckpt_path = rf'E:\BDCN-master\checkpoints\{folder}\{epoch}\{epoch}_model.pth'
        class_model.load_state_dict(torch.load(class_ckpt_path, map_location=torch.device('cpu')))

        # 保存结果的路径
        res_dir = rf'E:\BDCN-master\result\{folder}\{epoch}'
        if not os.path.exists(res_dir):
            os.makedirs(res_dir)

        test(bdcn_model, class_model, data_root, res_dir)


if __name__ == '__main__':
    main()

    
