 # 将预测结果乘以 255
    fore_ground = fore_ground * 255
    fore_ground = fore_ground.byte()  # 转换为字节格式

    # 选择第一张图像（如果存在多个批次）
    fore_ground_img = fore_ground[0]

    # 将 Tensor 转换为 NumPy 数组
    fore_ground_img = fore_ground_img.numpy()

    # 将 NumPy 数组转换为 PIL 图像
    pil_img = Image.fromarray(fore_ground_img, mode='L')

    # 保存灰度图像
    pil_img.save('foreground.png')
