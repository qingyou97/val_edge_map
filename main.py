# 读取黑白图像
img_anno = cv2.imread('./12_filtered.png', cv2.IMREAD_GRAYSCALE)

# 将黑白图像转换为BGR彩色图像
img_anno = cv2.cvtColor(img_anno, cv2.COLOR_GRAY2BGR)

# 坐标列表 (假设添加了坐标)
coords = [(10, 10), (20, 20), (30, 30)]

# 遍历所有坐标并标记红色点
for item in coords:
    x = item[0]
    y = item[1]
    print(f'x: {x}, y: {y}')
    img_anno[y, x] = (0, 0, 255)  # BGR通道，红色

# 保存新的图像
output_path = 'annotated_images.png'
cv2.imwrite(output_path, img_anno)
