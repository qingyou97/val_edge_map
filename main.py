import numpy as np
import torch
import torch.optim as optim
import torch.nn as nn
from torch.autograd import Variable
from torch.nn import functional as F
import argparse
import time
import re
import os
import sys
import bdcn
from datasets.dataset import Data
import cfg
import log
import cv2

from sklearn.metrics import precision_recall_curve


def adjust_learning_rate(optimizer, steps, step_size, gamma=0.1, logger=None):
    """Sets the learning rate to the initial LR decayed by 10 every 30 epochs"""

    for param_group in optimizer.param_groups:
        param_group['lr'] = param_group['lr'] * gamma
        if logger:
            logger.info('%s: %s' % (param_group['name'], param_group['lr']))


def cross_entropy_loss2d(inputs, targets, cuda=False, balance=1.1):
    """
    :param inputs: inputs is a 4 dimensional data nx1xhxw
    :param targets: targets is a 3 dimensional data nx1xhxw
    :return:
    """
    n, c, h, w = inputs.size()
    weights = np.zeros((n, c, h, w))
    for i in range(n):
        t = targets[i, :, :, :].cpu().data.numpy()
        pos = (t == 1).sum()
        neg = (t == 0).sum()
        valid = neg + pos
        weights[i, t == 1] = neg * 1. / valid
        weights[i, t == 0] = pos * balance / valid
    weights = torch.Tensor(weights)
    if cuda:
        weights = weights.cuda()
    inputs = F.sigmoid(inputs)
    # print(f'inputs:{inputs.shape}') # inputs:torch.Size([1, 1, 512, 512])
    # print(f'targets:{targets.shape}') # targets:torch.Size([1, 1, 512, 512])
    loss = nn.BCELoss(weights, size_average=False)(inputs, targets)
    return loss


def train(model, args):
    data_root = cfg.config[args.dataset]['data_root']
    data_lst = cfg.config[args.dataset]['data_lst']
    if 'Multicue' in args.dataset:
        data_lst = data_lst % args.k
    mean_bgr = np.array(cfg.config[args.dataset]['mean_bgr'])
    yita = args.yita if args.yita else cfg.config[args.dataset]['yita']
    crop_size = args.crop_size
    train_img = Data(data_root, data_lst, yita, mean_bgr=mean_bgr, crop_size=crop_size)
    trainloader = torch.utils.data.DataLoader(train_img, batch_size=args.batch_size, shuffle=True, num_workers=5)

    params_dict = dict(model.named_parameters())
    base_lr = args.base_lr
    weight_decay = args.weight_decay
    logger = args.logger
    params = []
    for key, v in params_dict.items():
        if re.match(r'conv[1-5]_[1-3]_down', key):
            if 'weight' in key:
                params += [{'params': v, 'lr': base_lr * 0.1, 'weight_decay': weight_decay * 1, 'name': key}]
            elif 'bias' in key:
                params += [{'params': v, 'lr': base_lr * 0.2, 'weight_decay': weight_decay * 0, 'name': key}]
        elif re.match(r'.*conv[1-4]_[1-3]', key):
            if 'weight' in key:
                params += [{'params': v, 'lr': base_lr * 1, 'weight_decay': weight_decay * 1, 'name': key}]
            elif 'bias' in key:
                params += [{'params': v, 'lr': base_lr * 2, 'weight_decay': weight_decay * 0, 'name': key}]
        elif re.match(r'.*conv5_[1-3]', key):
            if 'weight' in key:
                params += [{'params': v, 'lr': base_lr * 100, 'weight_decay': weight_decay * 1, 'name': key}]
            elif 'bias' in key:
                params += [{'params': v, 'lr': base_lr * 200, 'weight_decay': weight_decay * 0, 'name': key}]
        elif re.match(r'score_dsn[1-5]', key):
            if 'weight' in key:
                params += [{'params': v, 'lr': base_lr * 0.01, 'weight_decay': weight_decay * 1, 'name': key}]
            elif 'bias' in key:
                params += [{'params': v, 'lr': base_lr * 0.02, 'weight_decay': weight_decay * 0, 'name': key}]
        elif re.match(r'upsample_[248](_5)?', key):
            if 'weight' in key:
                params += [{'params': v, 'lr': base_lr * 0, 'weight_decay': weight_decay * 0, 'name': key}]
            elif 'bias' in key:
                params += [{'params': v, 'lr': base_lr * 0, 'weight_decay': weight_decay * 0, 'name': key}]
        elif re.match(r'.*msblock[1-5]_[1-3]\.conv', key):
            if 'weight' in key:
                params += [{'params': v, 'lr': base_lr * 1, 'weight_decay': weight_decay * 1, 'name': key}]
            elif 'bias' in key:
                params += [{'params': v, 'lr': base_lr * 2, 'weight_decay': weight_decay * 0, 'name': key}]
        else:
            if 'weight' in key:
                params += [{'params': v, 'lr': base_lr * 0.001, 'weight_decay': weight_decay * 1, 'name': key}]
            elif 'bias' in key:
                params += [{'params': v, 'lr': base_lr * 0.002, 'weight_decay': weight_decay * 0, 'name': key}]

    optimizer = torch.optim.SGD(params, momentum=args.momentum, lr=args.base_lr, weight_decay=args.weight_decay)
    # optimizer = optim.Adam(params, lr=args.base_lr, betas=(0.9, 0.999), eps=1e-08, weight_decay=args.weight_decay)

    start_step = 1
    mean_loss = []
    cur = 0
    pos = 0
    data_iter = iter(trainloader)
    iter_per_epoch = len(trainloader)
    logger.info('*' * 40)
    logger.info('train images in all are %d ' % iter_per_epoch)
    logger.info('*' * 40)
    for param_group in optimizer.param_groups:
        if logger:
            logger.info('%s: %s' % (param_group['name'], param_group['lr']))

    start_time = time.time()
    if args.cuda:
        model.cuda()
    if args.resume:
        logger.info('resume from %s' % args.resume)
        state = torch.load(args.resume)
        start_step = state['step']
        optimizer.load_state_dict(state['solver'])
        model.load_state_dict(state['param'])

    model.train()
    batch_size = args.iter_size * args.batch_size
    time_cost = []

    for step in range(start_step, args.max_iter + 1):
        print(f'epoch:{step}')
        batch_start_time = time.time()
        optimizer.zero_grad()
        batch_loss = 0
        for i in range(args.iter_size):
            if cur == iter_per_epoch:
                cur = 0
                data_iter = iter(trainloader)
            images, labels = next(data_iter)
            if args.cuda:
                images, labels = images.cuda(), labels.cuda()
            images, labels = Variable(images), Variable(labels)
            out = model(images)
            loss = 0
            for k in range(10):
                loss += args.side_weight * cross_entropy_loss2d(out[k], labels, args.cuda, args.balance) / batch_size
            loss += args.fuse_weight * cross_entropy_loss2d(out[-1], labels, args.cuda, args.balance) / batch_size
            loss.backward()
            # update parameter
            optimizer.step()
            batch_loss += loss.item()
            cur += 1

        print(f'batch_loss:{batch_loss}')

        if len(mean_loss) < args.average_loss:
            mean_loss.append(batch_loss)
        else:
            mean_loss[pos] = batch_loss
            pos = (pos + 1) % args.average_loss
        if step % args.step_size == 0:
            adjust_learning_rate(optimizer, step, args.step_size, args.gamma)
        if step % args.snapshots == 0:
            torch.save(model.state_dict(), '%s/bdcn_%d.pth' % (args.param_dir, step))
            state = {'step': step + 1, 'param': model.state_dict(), 'solver': optimizer.state_dict()}
            torch.save(state, '%s/bdcn_%d.pth.tar' % (args.param_dir, step))
        if step % args.display == 0:
            tm = time.time() - start_time
            logger.info('iter: %d, lr: %e, loss: %f, time using: %f(%fs/iter)' % (step,
                                                                                  optimizer.param_groups[0]['lr'],
                                                                                  np.mean(mean_loss), tm,
                                                                                  tm / args.display))

        batch_end_time = time.time()
        print(f'batch {step} training time:{batch_end_time - batch_start_time}')

    print(f'training end')


def main():
    args = parse_args()
    logger = log.get_logger(args.log)
    args.logger = logger
    logger.info('*' * 80)
    logger.info('the args are the below')
    logger.info('*' * 80)
    for x in args.__dict__:
        logger.info(x + ',' + str(args.__dict__[x]))
    logger.info(cfg.config[args.dataset])
    logger.info('*' * 80)
    os.environ['CUDA_VISIBLE_DEVICES'] = args.gpu
    if not os.path.exists(args.param_dir):
        os.mkdir(args.param_dir)
    torch.manual_seed(int(time.time()))
    model = bdcn.BDCN(pretrain=args.pretrain, logger=logger)
    if args.complete_pretrain:
        model.load_state_dict(torch.load(args.complete_pretrain, map_location=torch.device('cpu')))
    logger.info(model)

    train(model, args)


def parse_args():
    parser = argparse.ArgumentParser(description='Train BDCN for different args')
    parser.add_argument('-d', '--dataset', type=str, choices=cfg.config.keys(),
                        default='bsds500', help='The dataset to train')
    parser.add_argument('--param-dir', type=str, default='params/weight_decay002',
                        help='the directory to store the params')
    parser.add_argument('--lr', dest='base_lr', type=float, default=1e-6,
                        help='the base learning rate of model')
    parser.add_argument('-m', '--momentum', type=float, default=0.9,
                        help='the momentum')
    parser.add_argument('-c', '--cuda', action='store_true',
                        help='whether use gpu to train network')
    parser.add_argument('-g', '--gpu', type=str, default='0',
                        help='the gpu id to train net')
    parser.add_argument('--weight-decay', type=float, default=0.002,
                        help='the weight_decay of net')
    parser.add_argument('-r', '--resume', type=str, default=None,
                        help='whether resume from some, default is None')
    parser.add_argument('-p', '--pretrain', type=str, default=None,
                        help='init net from pretrained model default is None')
    # 默认：40000
    parser.add_argument('--max-iter', type=int, default=10000,
                        help='max iters to train network, default is 40000')
    parser.add_argument('--iter-size', type=int, default=4,
                        help='iter size equal to the batch size, default 10')
    parser.add_argument('--average-loss', type=int, default=50,
                        help='smoothed loss, default is 50')
    parser.add_argument('-s', '--snapshots', type=int, default=5,
                        help='how many iters to store the params, default is 1000')
    parser.add_argument('--step-size', type=int, default=10000,
                        help='the number of iters to decrease the learning rate, default is 10000')
    parser.add_argument('--display', type=int, default=20,
                        help='how many iters display one time, default is 20')
    parser.add_argument('-b', '--balance', type=float, default=1.1,
                        help='the parameter to balance the neg and pos, default is 1.1')
    parser.add_argument('-l', '--log', type=str, default='log.txt',
                        help='the file to store log, default is log.txt')
    parser.add_argument('-k', type=int, default=1,
                        help='the k-th split set of multicue')
    parser.add_argument('--batch-size', type=int, default=1,
                        help='batch size of one iteration, default 1')
    parser.add_argument('--crop-size', type=int, default=None,
                        help='the size of image to crop, default not crop')
    parser.add_argument('--yita', type=float, default=0.1,
                        help='the param to operate gt, default is data in the config file')
    parser.add_argument('--complete-pretrain', type=str,
                        default=r'E:\BDCN-master\BDCNmodel\bdcn_pretrained_on_bsds500.pth',
                        help='finetune on the complete_pretrain, default None')
    parser.add_argument('--side-weight', type=float, default=0.5,
                        help='the loss weight of sideout, default 0.5')
    parser.add_argument('--fuse-weight', type=float, default=1.1,
                        help='the loss weight of fuse, default 1.1')
    parser.add_argument('--gamma', type=float, default=0.1,
                        help='the decay of learning rate, default 0.1')
    return parser.parse_args()


def dice_loss(pred, target, smooth=1e-6):
    pred = torch.softmax(pred, dim=1)
    target = F.one_hot(target, num_classes=pred.shape[1]).permute(0, 3, 1, 2).float()
    intersection = (pred * target).sum(dim=(2, 3))
    union = pred.sum(dim=(2, 3)) + target.sum(dim=(2, 3))
    dice = (2. * intersection + smooth) / (union + smooth)
    return 1 - dice.mean()


def train_classifer(model, checkpoints_path, data_root, data_lst, save_ck_path, yita, num_classes, epoch, iter_size,
                    batch_size):
    from classifier_wider import FeatureExtractor
    import matplotlib.pyplot as plt
    import torch.nn.functional as F

    yita = yita  # 边缘像素阈值
    num_classes = num_classes  # 分类总数
    epoch_num = epoch
    iter_size = iter_size
    batch_size = batch_size
    beta = 1.1  # 负样本权重

    data_root = data_root  # 存放训练数据的路径
    data_lst = data_lst  # 训练数据路径下的train_pair.lst文件，里面的内容是相对data_root路径的图像和gt的相对路径
    save_ck_path = save_ck_path  # 存放checkpoints的相对路径
    if not os.path.exists(save_ck_path):
        os.makedirs(save_ck_path)

    # 加载训练
    train_img = Data(data_root, data_lst, yita)
    trainloader = torch.utils.data.DataLoader(train_img, batch_size=batch_size, shuffle=True, num_workers=5)

    data_iter = iter(trainloader)
    iter_per_epoch = len(trainloader)

    # 初始化模型
    base_model = model
    feature_extractor = FeatureExtractor(num_classes)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    base_model.to(device)
    feature_extractor.to(device)

    # 加载预训练模型
    if torch.cuda.is_available():
        state = torch.load(checkpoints_path, map_location='cuda')
    else:
        state = torch.load(checkpoints_path, map_location='cpu')
    base_model.load_state_dict(state)

    '''确认其他超参数的设置'''
    lr = 0.001
    optimizer = optim.Adam(feature_extractor.parameters(), lr=lr)
    # optimizer = optim.SGD(feature_extractor.parameters(), lr=0.01)

    # 设置学习率调度器, 每隔30个epoch，学习率降0.1倍
    # scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=30, gamma=0.1)
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, 'min')

    # 将 dataloader 放到外面
    def feature_maps_iterator(iter_size, iter_per_epoch, trainloader, data_iter, base_model):
        from torchvision import models, transforms

        # 加载 Wide ResNet-101-2 预训练模型
        wide_model = models.wide_resnet101_2(pretrained=True)
        wide_model.to(device)

        cur = 0
        img_list = []
        label_list = []
        feature_maps_list = []
        wide_list = []  # 保存特定层的输出

        for i in range(iter_size):
            print(f'数据处理中,当前迭代批次：{i}')
            if cur == iter_per_epoch:
                cur = 0
                data_iter = iter(trainloader)

            images, labels = next(data_iter)
            images, labels = images.to(device), labels.to(device)  # labels:torch.Size([1, 1, 512, 512]), 浮点数（0-1）

            # 计算原模型输出的feature maps
            base_model.eval()
            wide_model.eval()

            # 计算原模型输出的feature maps
            feature_maps = base_model(images)

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

            wide_model(images)
            wide_maps = []
            for layer, output in outputs.items():
                # print(f"Output of layer shape: {output.shape}")
                wide_maps.append(output)

            # 移除 hooks
            for hook in hooks:
                hook.remove()

            cur += 1
            img_list.append(images)
            label_list.append(labels)
            feature_maps_list.append(feature_maps)
            wide_list.append(wide_maps)
        return img_list, label_list, feature_maps_list, wide_list

    img_list, label_list, feature_maps_list, wide_list = feature_maps_iterator(iter_size, iter_per_epoch, trainloader,
                                                                               data_iter,
                                                                               base_model)

    cur = 0
    feature_extractor.train()
    train_losses = []

    for epoch in range(epoch_num):
        print(f'epoch:{epoch}')
        batch_loss = 0
        for images, labels, feature_maps, wide_maps in zip(img_list, label_list, feature_maps_list, wide_list):
            images, labels = images.requires_grad_(True), labels.requires_grad_(True)

            fused_map = feature_maps[-1]  # fused map

            wide_map_list = []
            wide1 = wide_maps[0]
            wide2 = wide_maps[1]
            wide3 = wide_maps[2]

            wide1.requires_grad_(True)
            wide2.requires_grad_(True)
            wide3.requires_grad_(True)

            wide_map_list.append(wide1)
            wide_map_list.append(wide2)
            wide_map_list.append(wide3)

            fused_map.requires_grad_(True)
            out = F.sigmoid(fused_map)  # 最终的输出图，像素值范围0-1

            feature_map = feature_extractor(wide_map_list)
            feature_map = F.sigmoid(feature_map)

            # 制作二分类标签
            new_label = labels

            # 制作二分类掩码
            num_positive = torch.sum(new_label == 1).float()
            num_negative = torch.sum(new_label == 0).float()

            mask = new_label.clone()
            mask[new_label == 1] = 1.0 * num_negative / (num_positive + num_negative)
            mask[new_label == 0] = 1.1 * num_positive / (num_positive + num_negative)
            mask = mask.detach()
            print(f'num_positive:{num_positive}')
            print(f'num_negative:{num_negative}')

            # 二分类损失函数
            loss = F.binary_cross_entropy(feature_map, new_label, weight=mask, reduction='sum')

            # 反向传播并优化
            optimizer.zero_grad()
            loss.backward(retain_graph=True)
            optimizer.step()

            batch_loss += loss.item()
            cur += 1
        train_losses.append(batch_loss)

        scheduler.step(loss)
        current_lr = optimizer.param_groups[0]['lr']
        print(f'lr:{current_lr}')
        print(f'Epoch [{epoch + 1}/{epoch_num}], Loss: {batch_loss:.4f}')

        if epoch % 1 == 0:
            # 保存模型阶段
            save_path = os.path.join(save_ck_path, f'{epoch}')
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            torch.save(feature_extractor.state_dict(), os.path.join(save_path, f'{epoch}_model.pth'))

    epochs = range(1, epoch_num + 1)

    # 创建图表
    plt.figure(figsize=(10, 5))
    plt.plot(epochs, train_losses, label='Training Loss')

    # 添加标题和标签
    plt.title('Training Loss per Epoch 0.001')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')

    # 显示网格
    plt.grid(True)

    # 显示图例
    plt.legend()

    # 保存图表到文件
    os.makedirs(os.path.join(r'E:\BDCN-master\result', f'{save_ck_path.split("/")[-1]}'), exist_ok=True)
    fig_path = os.path.join(r'E:\BDCN-master\result', f'{save_ck_path.split("/")[-1]}', f'lr{str(lr)}training_loss.png')
    plt.savefig(fig_path)

    # 显示图表
    plt.show()


if __name__ == '__main__':
    # main()
    model = bdcn.BDCN()
    checkpoints_path = r'E:\BDCN-master\BDCNmodel\bdcn_pretrained_on_bsds500.pth'
    data_root = r'E:\BDCN-master\traindata\one_cast'  # 存放训练数据的路径
    data_lst = 'train_pair.lst'  # 训练数据路径下的train_pair.lst文件，里面的内容是相对data_root路径的图像和gt的相对路径
    save_ck_path = 'checkpoints/3class_wide'

    yita = 0.3  # 边缘像素阈值
    num_classes = 3  # 分类总数
    epoch = 300
    iter_size = 1
    batch_size = 1
    train_classifer(model, checkpoints_path, data_root, data_lst, save_ck_path, yita, num_classes, epoch, iter_size,
                    batch_size)
