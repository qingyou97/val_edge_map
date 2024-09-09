import matplotlib.pyplot as plt
import numpy as np

def plot_matches(image0, image1, points0, points1):
    # 将图像转换为numpy格式
    image0_np = image0.cpu().numpy().transpose(1, 2, 0)  # convert (3,H,W) -> (H,W,3)
    image1_np = image1.cpu().numpy().transpose(1, 2, 0)

    # 创建合并图像，左右并行显示 input images
    height = max(image0_np.shape[0], image1_np.shape[0])
    width = image0_np.shape[1] + image1_np.shape[1]
    composite_image = np.zeros((height, width, 3))

    composite_image[:image0_np.shape[0], :image0_np.shape[1], :] = image0_np
    composite_image[:image1_np.shape[0], image0_np.shape[1]:, :] = image1_np

    # 调整点坐标, 在框取合成图上，特征点1需偏移以匹配image_1的位置
    points1_adj = points1.clone().numpy()
    points1_adj[:, 0] += image0_np.shape[1]

    # 作图
    fig, ax = plt.subplots(figsize=(18,9))
    ax.imshow(composite_image)

    # 绘制点及匹配线条
    for (pt0, pt1) in zip(points0.cpu().numpy(), points1_adj):
        color = np.random.rand(3)
        ax.scatter(*pt0, s=10, facecolors=color, edgecolors='k')
        ax.scatter(*pt1, s=10, facecolors=color, edgecolors='k')
        ax.plot([pt0[0], pt1[0]], [pt0[1], pt1[1]], color=color, linewidth=1.5)

    ax.axis('off')
    plt.show()

# 调用到函数的是,例如以下方法
plot_matches(image0, image1, points0, points1)
