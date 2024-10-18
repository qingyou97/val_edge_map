# 调整图像尺寸，例如放大到原来的两倍
img_resized = cv2.resize(img_anno, (img_anno.shape[1] * 2, img_anno.shape[0] * 2))
