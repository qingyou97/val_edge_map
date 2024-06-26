import numpy as np
import cv2
import os

# 计算 Precision, Recall, 和 F measure
def compute_rpf(cnt_r, sum_r, cnt_p, sum_p):
    R = np.divide(cnt_r, np.maximum(np.spacing(1), sum_r))
    P = np.divide(cnt_p, np.maximum(np.spacing(1), sum_p))
    F = 2 * P * R / np.maximum(np.spacing(1), P + R)
    return R, P, F

# 寻找优化的阈值，使得 F 值最大
def find_best_rpf(T, R, P):
    if len(T) == 1:
        bstT, bstR, bstP = T[0], R[0], P[0]
        bstF = 2 * P * R / np.maximum(np.spacing(1), P + R)
        return bstR, bstP, bstF, bstT

    A = np.linspace(0, 1, 100)
    bstF = -1
    for j in range(1, len(T)):
        Rj = R[j] * A + R[j-1] * (1 - A)
        Pj = P[j] * A + P[j-1] * (1 - A)
        Tj = T[j] * A + T[j-1] * (1 - A)
        Fj = 2 * Pj * Rj / np.maximum(np.spacing(1), Pj + Rj)
        max_f_index = np.argmax(Fj)
        f_max = Fj[max_f_index]
        if f_max > bstF:
            bstT = Tj[max_f_index]
            bstR = Rj[max_f_index]
            bstP = Pj[max_f_index]
            bstF = f_max
    return bstR, bstP, bstF, bstT

def process_images(pred_dir, gt_dir, thresholds=np.arange(0, 1.05, 0.05)):
    cntR, cntP = [], []
    sumR, sumP = [], []

    for file_name in os.listdir(pred_dir):
        gt_path = os.path.join(gt_dir, file_name)
        pred_path = os.path.join(pred_dir, file_name)

        gt_img = cv2.imread(gt_path, 0) // 255
        pred_img = cv2.imread(pred_path, 0) / 255.0

        sum_r = np.sum(gt_img)
        sumR.append(sum_r)

        cnt_r = [np.sum((pred_img >= t) & (gt_img == 1)) for t in thresholds]
        cntR.append(cnt_r)

        sum_p = [np.sum(pred_img >= t) for t in thresholds]
        sumP.append(sum_p)

    cntR = np.sum(np.array(cntR), axis=0)
    sumR = np.sum(np.array(sumR))
    cntP = np.sum(np.array(cntP), axis=0)
    sumP = np.sum(np.array(sumP))

    R, P, F = compute_rpf(cntR, sumR, cntP, sumP)
    _, _, bestF, bestT = find_best_rpf(thresholds, R, P)

    return bestT, bestF, P, R

pred_dir = "path_to_predicted_images"
gt_dir = "path_to_ground_truth_images"
bestT, bestF, P, R = process_images(pred_dir, gt_dir)

print(f"Best threshold: {bestT}")
print(f"Best F-score: {bestF}")
print(f"Precision: {P}")
print(f"Recall: {R}")
