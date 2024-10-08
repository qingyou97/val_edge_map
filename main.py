# 转换到 HSV 颜色空间
hsv = np.zeros((direction.shape[0], direction.shape[1], 3), dtype=np.uint8)
hsv[..., 0] = (direction - direction.min()) / (direction.max() - direction.min()) * 179  # H (色调)
hsv[..., 1] = 255  # S (饱和度)
hsv[..., 2] = 255  # V (数值)

# 转换为 BGR 颜色空间，以便保存和显示
bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# 保存图像并显示
cv2.imwrite('edge_direction.png', bgr)
