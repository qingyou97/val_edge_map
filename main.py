import cv2
import numpy as np
import time

def show_image(img, re=True):
    if re:
        img = cv2.resize(img, (1920, 1080))
    
    cv2.namedWindow("Image", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Image", img)
    cv2.moveWindow("Image", 0, 0)
    cv2.waitKey(0)

def main():
    image = cv2.imread("你的图片路径", 0)  # 以灰度模式读取图像
    if image is None:
        return -1
    
    origin = image.copy()
    show_image(image)

    start = time.time()
    element_open = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (17, 17))
    image = cv2.morphologyEx(image, cv2.MORPH_OPEN, element_open)
    end = time.time()
    print("open image time: {:.2f}ms".format((end - start) * 1000))
    show_image(image)

    start = time.time()
    element_close = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, element_close)
    end = time.time()
    print("close image time: {:.2f}ms".format((end - start) * 1000))
    show_image(image)

    start = time.time()
    _, image = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
    end = time.time()
    print("threshold image time: {:.2f}ms".format((end - start) * 1000))
    show_image(image)

    start = time.time()
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float32)
    image = cv2.filter2D(image, -1, kernel)
    end = time.time()
    print("filter2D image time: {:.2f}ms".format((end - start) * 1000))
    show_image(image)

    start = time.time()
    contours, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    end = time.time()
    print("findContours image time: {:.2f}ms".format((end - start) * 1000))

    img_contours = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    start = time.time()
    cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 1)  # 画出所有轮廓
    end = time.time()
    print("drawContours image time: {:.2f}ms".format((end - start) * 1000))
    show_image(img_contours)

    target_area = np.pi * 1400 * 1400
    result_contours = []

    start = time.time()
    for contour in contours:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        circularity = (4 * np.pi * area) / (perimeter * perimeter)
        if not (target_area * 0.25 <= area <= target_area * 1.44):
            continue
        result_contours.append(contour)

    result = np.zeros_like(img_contours)
    cv2.drawContours(result, result_contours, -1, (0, 0, 255), 2)
    end = time.time()
    print("draw resultContours image time: {:.2f}ms".format((end - start) * 1000))
    show_image(result)

    if not result_contours:
        return -1
    
    for contour in result_contours:
        ellipse = cv2.fitEllipse(contour)
        if origin.ndim == 2:  # 如果是灰度图，将其转换为彩色图
            origin = cv2.cvtColor(origin, cv2.COLOR_GRAY2BGR)
        color = (np.random.randint(256), np.random.randint(256), np.random.randint(256))
        cv2.ellipse(origin, ellipse, color, 2)
        show_image(origin)
    
    return 0

if __name__ == "__main__":
    main()
