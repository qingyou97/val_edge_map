def train_classifer(model, checkpoints_path, data_root, data_lst, save_ck_path, yita, num_classes, epoch, iter_size,
                    batch_size):
    from classifier import FeatureExtractor

    yita = yita  # 边缘像素阈值
    num_classes = num_classes  # 分类总数
    epoch_num = epoch
    iter_size = iter_size
    batch_size = batch_size
    beta = 0.1

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

    # 冻结 base_model 中的参数
    for param in base_model.parameters():
        param.requires_grad = False

    '''确认其他超参数的设置'''
    optimizer = optim.Adam(feature_extractor.parameters(), lr=1)

    # 将 dataloader 放到外面
    def feature_maps_iterator(iter_size, iter_per_epoch, trainloader, data_iter, base_model):
        cur = 0
        img_list = []
        label_list = []
        feature_maps_list = []
        for i in range(iter_size):
            print(f'数据处理中,当前迭代批次：{i}')
            if cur == iter_per_epoch:
                cur = 0
                data_iter = iter(trainloader)

            images, labels = next(data_iter)
            images, labels = images.to(device), labels.to(device)  # labels:torch.Size([1, 1, 512, 512]), 浮点数（0-1）

            # 计算原模型输出的fuse_map
            feature_maps = base_model(images)
            cur += 1
            img_list.append(images)
            label_list.append(labels)
            feature_maps_list.append(feature_maps)
        return img_list, label_list, feature_maps_list

    img_list, label_list, feature_maps_list = feature_maps_iterator(iter_size, iter_per_epoch, trainloader, data_iter,
                                                                    base_model)

    cur = 0
    feature_extractor.train()
    for epoch in range(epoch_num):
        batch_loss = 0

        for images, labels, feature_maps in zip(img_list, label_list, feature_maps_list):
            images, labels = images.requires_grad_(True), labels.requires_grad_(True)
            fused_map = feature_maps[-1]
            fused_map.requires_grad_(True)
            out = F.sigmoid(fused_map)  # 最终的输出图，像素值范围0-1

            '''确认是否需要激活'''
            feature_map = feature_extractor(fused_map)
            map = F.sigmoid(feature_map)  # 0-1
            map.requires_grad_(True)

            # 制作标签
            labels_shape = labels.shape
            label = torch.zeros(labels_shape)

            label[(labels == 1)] = 1  # (out >= yita) 和 (out < yita)
            label[(out >= yita) & (labels < 1)] = 0
            label[(out < yita) & (labels < 1)] = 2

            new_label = label.squeeze(1)
            new_label.requires_grad = True
            new_label = new_label.long()

            # 制作掩码
            mask = np.zeros(num_classes)

            num_class0 = torch.sum(new_label == 0).float()
            num_class1 = torch.sum(new_label == 1).float()
            num_class2 = torch.sum(new_label == 2).float()

            mask[0] = 1.0 * num_class2 / (num_class0 + num_class1 + num_class2)
            mask[1] = beta * num_class2 / (num_class0 + num_class1 + num_class2)
            mask[2] = num_class0 / (num_class0 + num_class1 + num_class2)
            mask = torch.tensor(mask, dtype=torch.float)
            mask = mask.detach()

            # 损失函数
            criterion = nn.CrossEntropyLoss(weight=mask)
            loss = criterion(map, new_label)

            # 反向传播并优化
            optimizer.zero_grad()
            loss.backward()

            batch_loss += loss.item()
            cur += 1

        optimizer.step()
        print(f'Epoch [{epoch + 1}/{epoch_num}], Loss: {loss.item():.4f}')

        # 保存模型阶段
        save_path = os.path.join(save_ck_path, f'{epoch}')
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        torch.save(model.state_dict(), os.path.join(save_path,f'{epoch}_model.pth'))
