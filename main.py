if __name__ == '__main__':
    # main()
    model = bdcn.BDCN()
    checkpoints_path = r'E:\BDCN-master\BDCNmodel\bdcn_pretrained_on_bsds500.pth'
    data_root = r'E:\BDCN-master\testdata'  # 存放训练数据的路径
    data_lst = 'train_pair.lst'  # 训练数据路径下的train_pair.lst文件，里面的内容是相对data_root路径的图像和gt的相对路径
    save_ck_path = 'checkpoints'

    yita = 0.4  # 边缘像素阈值
    num_classes = 3  # 分类总数
    epoch = 50
    iter_size = 2
    batch_size = 1

    train_classifer(model, checkpoints_path, data_root, data_lst, save_ck_path, yita, num_classes, epoch, iter_size,
                    batch_size)
