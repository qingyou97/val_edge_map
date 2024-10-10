# 调整窗口大小
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Image', 800, 600)  # 例如，设置窗口大小为800x600

# 显示图像
cv2.imshow('Image', image)

# 等待键盘输入以便关闭显示窗口
cv2.waitKey(0)

# 销毁所有窗口
cv2.destroyAllWindows()
