# 读取灰度图
img = cv2.imread('your_image_path', cv2.IMREAD_GRAYSCALE)

# 创建一个与图像大小相同的全黑图像
masked_img = np.zeros_like(img)

# 定义点的坐标列表
points = [(x1, y1), (x2, y2), (x3, y3), ...]

# 保留坐标点的灰度值
for (x, y) in points:
    masked_img[y, x] = img[y, x]

# 保存或者展示处理后的图像
cv2.imwrite('masked_image.png', masked_img)
# 或者使用 cv2.imshow('Masked Image', masked_img), 然后 cv2.waitKey(0) 显示图像窗口
