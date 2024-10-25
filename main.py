import cv2
import numpy as np
def normalized_cross_correlation(gray_image, template):
    threshold = 200
    image_height, image_width = gray_image.shape
    template_height, template_width = template.shape

    result_height = image_height - template_height + 1
    result_width = image_width - template_width + 1
    result = np.zeros((result_height, result_width))

    # Iterating over every location in the image where the template can fit
    for y in range(result_height):
        for x in range(result_width):
            image_patch = gray_image[y:y + template_height, x:x + template_width]

            # 计算白色像素的个数
            white_pixel_count = np.sum(image_patch >= threshold)

            # 计算白色像素的占比
            percent = white_pixel_count / (template_height * template_width)

            result[y, x] = percent

    return result


def get_rectangle_coordinates(image, A, h, w):
    rows, cols = image.shape
    x, y = A

    # Check if the rectangle is within the image boundaries
    if x + h > rows or y + w > cols:
        raise ValueError("The rectangle exceeds image boundaries")

    coordinates_set = set()

    for i in range(h):
        for j in range(w):
            coordinates_set.add((x + i, y + j))

    return coordinates_set


def boundingRect(image):

    # 寻找轮廓
    contours, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    img = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    lines = []
    center = []
    # 遍历轮廓并绘制外接矩形
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        A = (y,x)
        # line = get_rectangle_coordinates(image, A, h, w)
        # lines.append(line)
        center.append([(x, y),w,h])

    # 显示结果
    cv2.imshow('Ver Bounding Rectangles', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return center, img

def hor_boundingRect(image,hor_class):

    # 寻找轮廓
    contours, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    img = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    lines = []
    S = []
    center = []
    # 遍历轮廓并绘制外接矩形
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        A = (y,x)
        # 计算矩形的面接
        s = w * h
        print(f's：{s}')
        S.append(s)
        # line = get_rectangle_coordinates(image, A, h, w)
        # lines.append(line)


    # 找到前矩形面积的前8名
    indices = np.argpartition(S, -hor_class)[-hor_class:]
    top8_indices = indices[np.argsort(-np.array(S)[indices])]
    top8_s = [S[i] for i in top8_indices]

    # top8_lines = [lines[i] for i in top8_indices]

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        # 计算矩形的面接
        s = w * h
        if s in top8_s:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            center.append([(x,y),w,h])
    # 显示结果
    cv2.imshow('HOR_Bounding Rectangles', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return center, img

def save_hor_ver_lines(ai_path, shape, threshold, result_path,hor_class):
    image = cv2.imread(ai_path, cv2.IMREAD_GRAYSCALE)
    if image.shape != (224, 224):
        image = cv2.resize(image, (224, 224))
    shape = (shape[1],shape[0])

    # 二值化
    _, image = cv2.threshold(image, 80, 255, cv2.THRESH_BINARY)

    # 创建一个大小为 (20, 2) 的白色矩形
    rec = np.ones(shape, dtype=np.uint8) * 255

    # 找到图中白色区域，并返回置信度分数
    result = normalized_cross_correlation(image, rec)
    print(f'unique result:{np.unique(result)}')

    # 打印置信度分数的最大值和最小值
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(f"Min Value: {min_val}, Max Value: {max_val}")

    loc = np.where(result >= threshold)

    img = image.copy()
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    # 得到所有竖直点的集合
    ver_set = set()
    for i, pt in enumerate(zip(*loc[::-1])):
        A = (pt[1],pt[0])
        h = rec.shape[0]
        w = rec.shape[1]
        vertical = get_rectangle_coordinates(image, A, h, w)
        ver_set.update(vertical)
        cv2.rectangle(img, pt, (pt[0] + rec.shape[1], pt[1] + rec.shape[0]), (255, 0, 0), -1)

        # 显示结果图像
        # cv2.imshow('Detected', img)
        # cv2.waitKey(0)

    # cv2.imwrite('Vertical.png', img)
    # cv2.destroyAllWindows()

    # 验证集合上的点是否都是竖直的
    img2 = image.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
    for point in ver_set:
        img2[point[0],point[1]] = (0,0,255)
    # cv2.imwrite('Vertical1.png', img2)

    # 将竖直的点另存
    ver_save = np.zeros_like(image)
    for point in ver_set:
        ver_save[point[0],point[1]] = (255)
    # cv2.imwrite('Vertical_single.png', ver_save)

    lines = []
    # 分别保存两条竖线
    ver_lines, ver_img = boundingRect(ver_save)
    for ver_line in ver_lines:
        lines.append((0,ver_line))

    # 去掉竖直的线
    hor_save = image.copy()
    if image.shape == ver_save.shape:
        # 找出相交的像素位置
        intersection = (image == ver_save)
        # 将相交的像素值设置为0
        hor_save[intersection] = 0

    # cv2.imwrite('hor_single.png', hor_save)

    # 保存横线
    hor_lines, hor_img = hor_boundingRect(hor_save,hor_class)
    for hor_line in hor_lines:
        lines.append((1, hor_line))

    result = cv2.bitwise_or(ver_img, hor_img)
    cv2.imwrite(result_path, result)

    return lines


if __name__ == '__main__':
    # 读取黑白图像
    ai_path = r'D:\Projects\edge_detection\rule_based\images\20241024-143812.jpg'
    result_path = 'BR.png'
    rec_shape = (3,15) # 宽 高
    threshold = 0.98
    hor_class = 9
    rectangles = save_hor_ver_lines(ai_path, rec_shape, threshold,result_path,hor_class)
    print(rectangles)
    # lines的格式（0/1,[center_point,w,h))
