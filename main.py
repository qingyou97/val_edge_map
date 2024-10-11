import cv2
import math

def cal_ang(start, center, end):
    """
    根据三点坐标计算夹角
    :param start: 点1坐标
    :param center: 点2坐标
    :param end: 点3坐标
    :return: 返回点2的夹角
    """
    a = math.sqrt((center[0] - end[0]) ** 2 + (center[1] - end[1]) ** 2)
    b = math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)
    c = math.sqrt((start[0] - center[0]) ** 2 + (start[1] - center[1]) ** 2)
    return math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))

def detect_and_draw_arc(image_path):
    # 读取图像
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # 查找轮廓凸包缺陷，确定圆弧起点和终点坐标
    hull = cv2.convexHull(contours[0], returnPoints=False)
    defects = cv2.convexityDefects(contours[0], hull)
    start = end = (0, 0)
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(contours[0][s][0])
        end = tuple(contours[0][e][0])
        if d > 5000:
            break

    # 获取轮廓最小外接圆，获取圆心，计算圆弧角度
    center, radius = cv2.minEnclosingCircle(contours[0])
    center = (int(center[0]), int(center[1]))
    radius = int(radius)

    # 使用红色标记圆心和检测到的圆弧
    cv2.circle(img, center, 8, (0, 0, 255), -1)  # 红色圆心
    cv2.circle(img, start, 8, (0, 0, 255), -1)  # 红色起点
    cv2.circle(img, end, 8, (0, 0, 255), -1)    # 红色终点

    # 画红色圆弧线
    angle_1 = cal_ang(start, center, (center[0] + 100, center[1]))
    angle_2 = cal_ang(end, center, (center[0] + 100, center[1]))
    cv2.ellipse(img, center, (radius, radius), 0, -angle_1, 0, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.ellipse(img, center, (radius, radius), 0, 0, angle_2, (0, 0, 255), 2, cv2.LINE_AA)

    # 显示结果
    cv2.imshow('result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 调用函数
detect_and_draw_arc('11.png')
