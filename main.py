for x, y in coords:
    image[y, x] = (0, 0, 255)  # 注意：OpenCV 图像的颜色顺序是 BGR (蓝绿红)，而不是 RGB

# 保存新的图像
output_path = 'output_image.jpg'
cv2.imwrite(output_path, image)
