#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@File  : point_predict
@Author: Wendy
@Time  : 2024/4/11 10:21
@Desc  :
"""
import cv2
import numpy as np
from demo import LightGlueMatch


def vision_angle_transformer(image1, frame_index, image1_point, image2, matching_save_path):
    image1 = cv2.imread(image1)
    image2 = cv2.imread(image2)
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    frame_com_kpts, frame_kpts = LightGlueMatch(gray1, gray2, frame_index, matching_save_path)
    if len(frame_com_kpts) >= 10:
        print('Meet matching points num')
        # 获得源和目标点的数组
        srcPts = np.float32(frame_com_kpts).reshape(-1, 1, 2)
        dstPts = np.float32(frame_kpts).reshape(-1, 1, 2)
        print(f'上一帧特征点的个数：{srcPts.shape[0]}')

        # 获得单应性矩阵H
        H, _ = cv2.findHomography(srcPts, dstPts, 0, 2.0)
        print("h:", H)

        image2_point = cv2.perspectiveTransform(image1_point, H)
        image2_point = np.squeeze(image2_point).tolist()
        print(f'上一帧的坐标:{np.squeeze(image1_point).tolist()}')
        print(f'单应性矩阵计算后的下一帧坐标:{image2_point}')

    return image2_point


if __name__ == '__main__':
    vision_angle_transformer(image1=r'D:\2. project\RAFT-master\frame_img/0.jpg', frame_index=0,
                             image1_point=[1611, 859],
                             image2=r'D:\2. project\RAFT-master\frame_img/1.jpg',
                             matching_save_path=r'./matching_save')
