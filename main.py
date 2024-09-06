 feature_map = feature_extractor(fused_map)
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
            mask[new_label == 1] = 2.0 * num_negative / (num_positive + num_negative)
            mask[new_label == 0] = 1.1 * num_positive / (num_positive + num_negative)
            mask = mask.detach()
            print(f'num_positive:{num_positive}')
            print(f'num_negative:{num_negative}')

            # 二分类损失函数
            loss = F.binary_cross_entropy(feature_map, new_label, weight=mask, reduction='sum')
