      
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
    mean_bgr = np.array([104.00699, 116.66877, 122.67892])

    test_root = data_root

    test_lst = os.listdir(test_root)

    save_dir = res_dir
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    bdcn_model.eval()

    start_time = time.time()
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

        out = [F.sigmoid(out[-1]).cpu().data.numpy()]
        save_out = [out[-1][0, 0, :, :]]

        fused_map = Variable(torch.tensor(out[-1]))
        feature_map = class_model(fused_map)
        # print(f'feature_map:{feature_map.shape}')
        class_map = torch.argmax(feature_map, dim=1)
        # print('class_map', torch.unique(class_map.detach()))
        unique_values, counts = torch.unique(class_map, return_counts=True)

        print(f"类   别: {unique_values}")
        print(f"类别个数: {counts}")
        save_class_map = torch.zeros_like(class_map)
        save_class_map[class_map != 1] = 1
        save_class_map = save_class_map.cpu().data.numpy()
        save_class_map = np.squeeze(save_class_map, axis=0)

        # 保存原模型的fused map
        if not os.path.exists(os.path.join(save_dir, 'fuse')):
            os.mkdir(os.path.join(save_dir, 'fuse'))
        cv2.imwrite(os.path.join(save_dir, 'fuse/%s.png' % nm.split('/')[-1].split('.')[0]), 255 - 255 * save_out[-1])

        # 保存经过分类之后的模型
        if not os.path.exists(os.path.join(save_dir, 'class')):
            os.mkdir(os.path.join(save_dir, 'class'))
        cv2.imwrite(os.path.join(save_dir, 'class/%s.png' % nm.split('/')[-1].split('.')[0]),
                    255 * save_class_map)

        all_t += time.time() - t1

    # print('infer time', all_t)
    # print('Overall Time use: ', time.time() - start_time)
    # print('len test_list', len(test_lst))
    # print('fps', len(test_lst) / all_t)


def main():
    import time
    from classifier import FeatureExtractor
    print(time.localtime())

    bdcn_ckpt_path = r'E:\BDCN-master\BDCNmodel\bdcn_pretrained_on_bsds500.pth'

    # 加载原模型
    bdcn_model = bdcn.BDCN()
    bdcn_model.load_state_dict(torch.load(bdcn_ckpt_path, map_location=torch.device('cpu')))

    # 加载分类模型
    num_classes = 3
    class_ckpt_path = r'E:\BDCN-master\checkpoints\casting\50\50_model.pth'
    class_model = FeatureExtractor(num_classes)
    class_model.load_state_dict(torch.load(class_ckpt_path, map_location=torch.device('cpu')))
    data_root = r'E:\BDCN-master\testdata\casting'
    res_dir = r'E:\BDCN-master\result\casting'
    test(bdcn_model, class_model, data_root, res_dir)


if __name__ == '__main__':
    main()

    
