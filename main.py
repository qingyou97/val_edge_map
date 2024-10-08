法1
1. 高斯模糊 (Gaussian Blur)：
- 函数: cv2.GaussianBlur(img_gray, ksize=（3，3）, sigmaX)
- 作用: 平滑图像，减少噪音。

2. Otsu阈值分割 (Otsu's Binarization)：
- 函数: cv2.threshold(img_blur, thresh=0, maxval=255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
- 作用: 自动计算最佳阈值以二值化图像。

3. 形态学操作 (Morphological Operations)：
  kernel = np.ones(shape:(3,3), np.uint8)
  - 开运算 (Opening):
    - 函数: cv2.morphologyEx(img_thresh, cv2.MORPH_OPEN, kernel)
    - 作用: 去除小的白色噪点。
  - 闭运算 (Closing):
    - 函数: cv2.morphologyEx(img_open, cv2.MORPH_CLOSE, kernel)
    - 作用: 填充小的黑色空洞。

4. 骨架化（Skeletonization）：
- 函数: skeletonize(img_close == 0)
- 使用库: from skimage.morphology import skeletonize
- 作用: 将图像的主轮廓提取成单像素宽的线条。

法2

1. 二值化图像：
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
  使用 cv2.threshold 对图像进行二值化处理，阈值为 127。低于此值的像素设为 0，高于此值的像素设为 255。

2. 创建形态学操作核：
kernel = np.ones((3,3), np.uint8)
  创建一个 3x3 的全1矩阵（由 uint8 类型的值组成），作为形态学操作中的卷积核。

4. 腐蚀操作：
eroded = cv2.erode(binary, kernel, iterations=1)
  使用 cv2.erode 减少边缘厚度。腐蚀操作迭代一次。
  
5. 骨架化函数：
def skeletonize(image):
    skel = np.zeros(image.shape, np.uint8)
    temp = np.zeros(image.shape, np.uint8)
    eroded = np.zeros(image.shape, np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))

    while True:
        eroded = cv2.erode(image, kernel)
        temp = cv2.dilate(eroded, kernel)
        temp = cv2.subtract(image, temp)
        skel = cv2.bitwise_or(skel, temp)
        image = eroded.copy()
        if cv2.countNonZero(image) == 0:
            break

    return skel
- kernel: 一个 3x3 的十字型结构核，由 cv2.getStructuringElement 创建。
- 骨架化具体步骤：
  1. 腐蚀操作：对图像进行腐蚀。
  2. 膨胀腐蚀结果：对腐蚀后的图像进行膨胀。
  3. 图像差：原图 - 膨胀后的图像。
  4. 更新骨架：将差值结果与当前骨架结果进行位或操作，更新骨架图像。
  5. 更新图像：图像被 eroded 的结果替换。
  6. 终止条件：直到没有非零像素为止。
