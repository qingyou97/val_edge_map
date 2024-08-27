if __name__ == '__main__':
    # main()
    model = bdcn.BDCN()
    checkpoints_path = r'E:\BDCN-master\BDCNmodel\bdcn_pretrained_on_bsds500.pth'
    train_classifer(model, checkpoints_path)
def train_classifer(model, checkpoints_path):
    from classifier import FeatureExtractor

    data_root = r'E:\BDCN-master\testdata'
    data_lst = 'train_pair.lst'
    mean_bgr = np.array([104.00699, 116.66877, 122.67892])
    yita = 0.4
    crop_size = None

    train_img = Data(data_root, data_lst, yita, mean_bgr=mean_bgr, crop_size=crop_size)
    trainloader = torch.utils.data.DataLoader(train_img, batch_size=1, shuffle=True, num_workers=5)

    cur = 0
    data_iter = iter(trainloader)
    iter_per_epoch = len(trainloader)

    beta  = 0.1

    # 初始化模型
    base_model = model
    # if args.cuda:
    #     base_model.cuda()
    feature_extractor = FeatureExtractor() # ??这个用不用cuda

    # 加载预训练模型
    state = torch.load(checkpoints_path, map_location='cpu')
    base_model.load_state_dict(state)

    # 冻结 base_model 中的参数
    for param in base_model.parameters():
        param.requires_grad = False

    # 定义损失函数和优化器，只优化分类器中的参数
    optimizer = torch.optim.SGD(feature_extractor.parameters(), momentum=0.9, lr=0.001, weight_decay=0.001)

    feature_extractor.train()
    # 训练循环
    for epoch in range(50):  # 假设有50个epoch
        optimizer.zero_grad()

        batch_loss = 0
        for i in range(2):
            if cur == iter_per_epoch:
                cur = 0
                data_iter = iter(trainloader)
            images, labels = next(data_iter)
            # if args.cuda:
            #     images, labels = images.cuda(), labels.cuda()
            images, labels = Variable(images), Variable(labels)
            print(f'labels:{labels.shape}') # labels:torch.Size([1, 1, 512, 512])
            # print(f'labels:{torch.unique(labels)}') # 浮点数（0-1）
            # 前向传播
            mask = np.zeros_like(labels, dtype=float)

            with torch.no_grad():  # base_model不需要梯度
                features = base_model(images)
                fused_map = features[-1]
                out = [F.sigmoid(fused_map).cpu().data.numpy()]
                out = out[-1] # 0-1

            feature_map = feature_extractor(fused_map) # ？？？确认是否需要激活
            map = [F.sigmoid(feature_map).cpu().data.numpy()]
            map = map[-1] # 0-1
            map = torch.tensor(map, requires_grad=True)


            labels[(labels >= yita)] =1
            labels[(labels < yita)] = 0

            fused_bin_map = np.zeros_like(out)
            fused_bin_map[(out >= yita)] = 1
            fused_bin_map[(out < yita)] = 0
            fused_bin_map = torch.Tensor(fused_bin_map)


            new_label = np.zeros_like(labels, dtype=float)
            new_label[(labels == 1)] = 1
            new_label[(fused_bin_map == 1) & (labels == 0)] = 0
            new_label[(fused_bin_map == 0)] = 0.5
            new_label = torch.tensor(new_label)

            num_positive_true = torch.sum(new_label == 1).float()
            num_negative_true = torch.sum(new_label == 0).float()

            # 制作掩码
            mask[new_label == 1] = 1.0 * num_negative_true / (num_negative_true + num_positive_true)
            mask[new_label == 0] = beta * num_positive_true / (num_negative_true + num_positive_true)
            mask[new_label == 0.5] = 0
            mask = torch.tensor(mask)
            mask = mask.detach()


            loss = F.binary_cross_entropy(
                map, labels, weight=mask, reduction='sum')
            print(f'loss:{loss}')
