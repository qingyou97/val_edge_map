      
import os
import subprocess

import cv2
import numpy as np

def calculate_metrics(true_image, detected_image):
    # 将图像转换为二值图像
    _, true_binary = cv2.threshold(true_image, 127, 255, cv2.THRESH_BINARY)
    _, detected_binary = cv2.threshold(detected_image, 127, 255, cv2.THRESH_BINARY)

    # 计算真阳性、假阳性和假阴性
    TP = np.sum((true_binary == 0) & (detected_binary == 0))
    FP = np.sum((true_binary == 255) & (detected_binary == 0))
    FN = np.sum((true_binary == 0) & (detected_binary == 255))

    # 计算精确率、召回率和F1-score
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    return precision, recall, f1_score

def infer_images(imgs_path, save_path, checkpoints_path):

    #
    cmd = f"python test_image.py  -c -g 0 --model {checkpoints_path} --res-dir {save_path} --data-root {imgs_path}  "
    print('cmd:', cmd)
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')

    # 实时输出标准输出和标准错误
    try:
        # 实时输出标准输出和标准错误
        for stdout_line in iter(process.stdout.readline, ''):
            print(stdout_line, end='')

        for stderr_line in iter(process.stderr.readline, ''):
            print(stderr_line, end='')

    finally:
        process.stdout.close()
        process.stderr.close()
        process.wait()

def infer_and_f1(imgs_path, save_path, checkpoints_path, img_results_folder, gt_path ):

    if not os.path.exists(save_path):
        os.makedirs(save_path, exist_ok=True)
    # 推理
    infer_images(imgs_path, save_path, checkpoints_path)

    # 计算precision等指标
    img_results_list = os.listdir(img_results_folder)

    infer_list = []
    for img in img_results_list:
        if '.png' in img:
            infer_list.append(img)

    gt_list = os.listdir(gt_path)
    precision_list = []
    recall_list = []
    f1_list = []
    for img in infer_list:
        infer_path = os.path.join(img_results_folder, img)
        print(f'infer_path:{infer_path}')
        gt_new_path = os.path.join(gt_path, img)
        print(f'gt_new_path:{gt_new_path}')
        gt = cv2.imread(gt_new_path, cv2.IMREAD_GRAYSCALE)
        infer_img = cv2.imread(infer_path, cv2.IMREAD_GRAYSCALE)
        if gt is not None:
            # infer_img = inverted_image = cv2.bitwise_not(infer_img)
            precision, recall, f1_score = calculate_metrics(gt, infer_img) # 白底黑边
            precision_list.append(precision)
            recall_list.append(recall)
            f1_list.append(f1_score)
        else:
            print('gt为None')
    precision_ave = sum(precision_list)/len(precision_list)
    recall_ave = sum(recall_list)/len(recall_list)
    f1_ave = sum(f1_list)/len(f1_list)

    return precision_ave, recall_ave, f1_ave

if __name__ == '__main__':
    # 推理
    imgs_path = r'E:\BDCN-master\testdata'
    checkpoints_path = r'E:\BDCN-master\BDCNmodel\bdcn_pretrained_on_bsds500.pth'
    save_path = r'E:\BDCN-master\result' # 白底黑边
    # 计算指标，注意边缘图是否都是黑底白边
    img_results_folder = save_path
    gt_path = r'E:\Datasets\BSDS_datasets_\BSDS500\data\GT_convert_0\train' # 白底黑边

    precision_ave, recall_ave, f1_ave = infer_and_f1(imgs_path, save_path, checkpoints_path, img_results_folder, gt_path )
    print(f'precision:{precision_ave}, recall:{recall_ave}, f1:{f1_ave}')

    
