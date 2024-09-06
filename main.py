def train_classifer_with_ori(model, checkpoints_path, data_root, data_lst, save_ck_path, yita, num_classes, epoch, iter_size,
                    batch_size):
    from classifier import FeatureExtractor
    from cross_dice_loss import CombinedLoss

    yita = yita  # 边缘像素阈值
    num_classes = num_classes  # 分类总数
    epoch_num = epoch
    iter_size = iter_size
    batch_size = batch_size
    beta = 1.1

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
    optimizer = optim.Adam(feature_extractor.parameters(), lr=0.001)
    # optimizer = optim.SGD(feature_extractor.parameters(), lr=0.01) #30epoch

    # 设置学习率调度器, 每隔30个epoch，学习率降0.1倍
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=30, gamma=0.1)

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

            feature_map = feature_extractor(images)
            feature_map = F.sigmoid(feature_map)

            # 制作三分类标签
            # labels_shape = labels.shape
            # label = torch.zeros(labels_shape)
            #
            # label[(labels == 1)] = 1  # (out >= yita) 和 (out < yita)
            # label[(out >= yita) & (labels < 1)] = 0
            # label[(out < yita) & (labels < 1)] = 2
            #
            # new_label = label.squeeze(1)
            # new_label.requires_grad = True
            # new_label = new_label.long()

            # 制作二分类标签
            new_label = labels

            # 查看gt
            # new = torch.squeeze(new_label, dim=0)
            # print(f'new shape:{new.shape}')
            # check_label = torch.zeros_like(new)
            # check_label[new == 1] = 1
            # check_label = check_label.numpy()
            # cv2.imwrite('label1.png', 255 * check_label)
            #
            # check_label1 = torch.zeros_like(new)
            # check_label1[new == 0] = 1
            # check_label1 = check_label1.numpy()
            # cv2.imwrite('label0.png', 255 * check_label1)
            #
            # check_label2 = torch.zeros_like(new)
            # check_label2[new == 2] = 1
            # check_label2 = check_label2.numpy()
            # cv2.imwrite('label2.png', 255 * check_label2)

            # 制作三分类掩码
            # mask = np.zeros(num_classes)

            # num_class0 = torch.sum(new_label == 0).float()
            # num_class1 = torch.sum(new_label == 1).float()
            # num_class2 = torch.sum(new_label == 2).float()
            # print(f'num_class0:{num_class0}')
            # print(f'num_class1:{num_class1}')
            # print(f'num_class2:{num_class2}')

            # mask[0] = 0.3
            # mask[1] = 0.3
            # mask[2] = 0.3
            # mask[0] = 0.5 * num_class2 / (num_class0 + num_class1 + num_class2)
            # mask[1] = 0.8 * num_class1 / (num_class0 + num_class1 + num_class2)
            # mask[2] = 0.5 * num_class0 / (num_class0 + num_class1 + num_class2)
            #
            # mask = torch.tensor(mask, dtype=torch.float)
            # mask = mask.detach()
            # print(f'mask:{mask}')

            # 多分类损失函数
            # criterion = nn.CrossEntropyLoss(weight=mask)
            # loss = criterion(feature_map, new_label) + dice_loss(feature_map, new_label)


            # 制作二分类掩码

            num_positive = torch.sum(new_label == 1).float()
            num_negative = torch.sum(new_label == 0).float()

            mask = new_label.clone()
            mask[new_label == 1] = 1.0 * num_negative / (num_positive + num_negative)
            mask[new_label == 0] = 10.1 * num_positive / (num_positive + num_negative)
            mask = mask.detach()
            print(f'num_positive:{num_positive}')
            print(f'num_negative:{num_negative}')

            # 二分类损失函数
            loss = F.binary_cross_entropy(feature_map, new_label, weight=mask, reduction='sum')

            # 反向传播并优化
            optimizer.zero_grad()
            loss.backward()

            batch_loss += loss.item()
            cur += 1

        optimizer.step()
        # scheduler.step()
        print(f'Epoch [{epoch + 1}/{epoch_num}], Loss: {loss.item():.4f}')

        if epoch % 1 == 0:
            # 保存模型阶段
            save_path = os.path.join(save_ck_path, f'{epoch}')
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            torch.save(feature_extractor.state_dict(), os.path.join(save_path, f'{epoch}_model.pth'))
