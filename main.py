# 读取黑白图1并获取白色像素的坐标
img1 = cv2.imread('path_to_image1.png', cv2.IMREAD_GRAYSCALE)
coords1 = np.column_stack(np.where(img1 > 0))

# 读取黑白图2并获取白色像素的坐标
img2 = cv2.imread('path_to_image2.png', cv2.IMREAD_GRAYSCALE)
coords2 = np.column_stack(np.where(img2 > 0))

# 读取图3
img3 = cv2.imread('path_to_image3.png')

# 复制图3以绘制红点
output_img = img3.copy()

# 将黑白图白色点的坐标使用红色绘制在图3上
for coord in coords1:
    cv2.circle(output_img, (coord[1], coord[0]), 1, (0, 0, 255), -1)
for coord in coords2:
    cv2.circle(output_img, (coord[1], coord[0]), 1, (0, 0, 255), -1)

# 显示结果图像
cv2.imshow('Output Image', output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存结果图像
cv2.imwrite('output_image.png', output_img)
