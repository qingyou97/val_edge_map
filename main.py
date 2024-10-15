import cv2
import math
import numpy as np


def angle_between_vectors(v1, v2):
    dot_product = sum(p * q for p, q in zip(v1, v2))
    magnitude_v1 = math.sqrt(sum(p ** 2 for p in v1))
    magnitude_v2 = math.sqrt(sum(q ** 2 for q in v2))
    cos_theta = dot_product / (magnitude_v1 * magnitude_v2)
    # 防止浮点误差导致的值域超出
    cos_theta = max(min(cos_theta, 1), -1)
    theta = math.acos(cos_theta)
    return math.degrees(theta)


def is_angle_less_than_15_degrees(A, B, C, thresh):
    # 向量 AB 和 AC
    AB = [B[0] - A[0], B[1] - A[1]]
    AC = [C[0] - A[0], C[1] - A[1]]
    angle = angle_between_vectors(AB, AC)
    print(f'angle:{angle}')
    return angle <= thresh


def are_collinear(A, B, C):
    # 计算向量AB和AC
    AB = (B[0] - A[0], B[1] - A[1])
    AC = (C[0] - A[0], C[1] - A[1])

    # 计算向量AB和AC的叉积
    cross_product = AB[0] * AC[1] - AB[1] * AC[0]

    # 如果叉积为零，表示三点共线
    return cross_product == 0


def compare_brightness(ori_path, A, B, C, angle_deg):
    # 获取亮度值
    gray = cv2.imread(ori_path, cv2.IMREAD_GRAYSCALE)
    gray = gray.astype(np.float32)

    if (angle_deg == 0) or (angle_deg == 360):
        b_B = gray[B[0], B[1] + 1]
        b_C = gray[C[0], C[1] + 1]

        if b_B > b_C:
            return B
        else:
            return C

    if (0 < angle_deg < 90):
        b_B = gray[B[0] + 1, B[1] + 1]
        b_C = gray[C[0] + 1, C[1] + 1]

        if b_B > b_C:
            return B
        else:
            return C

    if (angle_deg == 90):

        b_B = gray[B[0] + 1, B[1]]
        b_C = gray[C[0] + 1, C[1]]

        if b_B > b_C:
            return B
        else:
            return C



    elif (90 < angle_deg < 180):

        b_B = gray[B[0] + 1, B[1] - 1]
        b_C = gray[C[0] + 1, C[1] - 1]

        if b_B > b_C:
            return B
        else:
            return C

    elif (angle_deg == 180):

        b_B = gray[B[0], B[1] - 1]
        b_C = gray[C[0], C[1] - 1]

        if b_B > b_C:
            return B
        else:
            return C

    elif (180 < angle_deg < 270):

        b_B = gray[B[0] - 1, B[1] - 1]
        b_C = gray[C[0] - 1, C[1] - 1]

        if b_B > b_C:
            return B
        else:
            return C

    elif (angle_deg == 270):

        b_B = gray[B[0] - 1, B[1]]
        b_C = gray[C[0] - 1, C[1]]

        if b_B > b_C:
            return B
        else:
            return C

    elif (270 < angle_deg < 360):

        b_B = gray[B[0] - 1, B[1] + 1]
        b_C = gray[C[0] - 1, C[1] + 1]

        if b_B > b_C:
            return B
        else:
            return C



def save_brighter_coordinates(path, A, B, C, angle_thresh):
    if is_angle_less_than_15_degrees(A, B, C, angle_thresh):
        # if are_collinear(A, B, C): # 在三点为一条直线的情况下
        angle = calculate_angle(A, B)
        point = compare_brightness(path, A, B, C, angle)
        if point:
            print(f'save {point}')
    else:
        raise ValueError("两个峰值点与原点形成的角度太大")

    return point


def calculate_angle(X, Y):
    y1, x1 = X
    y2, x2 = Y
    dx = x2 - x1
    dy = y2 - y1
    angle = np.arctan2(dy, dx)  # 计算弧度
    angle_degrees = np.degrees(angle)  # 转换为度数
    if angle_degrees < 0:
        angle_degrees += 360
    return angle_degrees
