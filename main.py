import matplotlib.pyplot as plt
import torch

# 将图像加载换为CPU且变成numpy数组
image0_cpu = image0.squeeze().cpu().numpy().transpose(1, 2, 0)
image1_cpu = image1.squeeze().cpu().numpy().transpose(1, 2, 0)

# 画图
fig, ax = plt.subplots(1, 2, figsize=(15, 10))

# 绘制图像1的点
ax[0].imshow(image0_cpu)
ax[0].scatter(points0[:, 0], points0[:, 1], c='r', marker='o')
ax[0].title.set_text('Image 0 Keypoints')

# 绘制图像2的点
ax[1].imshow(image1_cpu)
ax[1].scatter(points1[:, 0], points1[:, 1], c='r', marker='o')
ax[1].title.set_text('Image 1 Keypoints')

# 在两图之间画连线
for p0, p1 in zip(points0, points1):
    fig.lines.append(plt.Line2D(
        [p0[0], p1[0] + image0_cpu.shape[1]], 
        [p0[1], p1[1]], 
        color='yellow'  # 线条颜色可以自己更改
    ))

# 拼接两幅图像
combined_image = torch.cat((image0, image1), dim=2).squeeze().cpu().numpy().transpose(1, 2, 0)
ax_combined = fig.add_subplot(111, frameon=False)
ax_combined.imshow(combined_image)
ax_combined.axis('off')
ax_combined.title.set_text('Correspondences')

plt.show()
