def eliminate(image_path, save_path):
    # 读取灰度图
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 二值化
    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    ori = img.copy()

    # 先腐蚀操作后膨胀操作
    kernel = np.ones((2, 2), np.uint8)
    img = cv2.erode(img, kernel, iterations=1)  # 程度重
    img = cv2.dilate(img, kernel, iterations=1)

    # 滤波
    img = cv2.medianBlur(img, 3)  # 程度轻

    # 保存结果
    cv2.imwrite(save_path, img)

    # 显示结果
    cv2.imshow('Original Image', ori)
    cv2.imshow('After Erosion and Dilation', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = r'D:\Projects\edge_detection\rule_based\images\20241017-173513.jpg'
save_path = r'a.png'
eliminate(image_path, save_path)
