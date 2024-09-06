def test(bdcn_model, class_model, data_root, res_dir):
    mean_bgr = np.array([104.00699, 116.66877, 122.67892])

    test_root = data_root

    test_lst = os.listdir(test_root)

    save_dir = res_dir
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    bdcn_model.eval()
    class_model.eval()

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

        fused_map = out[-1].cpu().data

        out = [F.sigmoid(out[-1]).cpu().data.numpy()]
        save_out = [out[-1][0, 0, :, :]]

        fused_map = Variable(torch.tensor(fused_map))
        feature_map = class_model(fused_map)


        class_map = F.sigmoid(feature_map).cpu().data.numpy()[0, 0, :, :]

        # 保存原模型的fused map
        if not os.path.exists(os.path.join(save_dir, 'fuse')):
            os.mkdir(os.path.join(save_dir, 'fuse'))
        cv2.imwrite(os.path.join(save_dir, 'fuse/%s.png' % nm.split('/')[-1].split('.')[0]), 255 - 255 * save_out[-1])

        # 保存经过分类之后的模型
        if not os.path.exists(os.path.join(save_dir, 'class_1')):
            os.mkdir(os.path.join(save_dir, 'class_1'))

        cv2.imwrite(os.path.join(save_dir, 'class_1/%s.png' % nm.split('/')[-1].split('.')[0]),
                    255- 255 * class_map)

        all_t += time.time() - t1
