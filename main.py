      
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
    cmd = f"python main.py --model pidinet_converted --gpu 0 --config carv4 --sa --dil -j 4 --savedir {save_path} --datadir {imgs_path} --dataset Custom --evaluate {checkpoints_path} --evaluate-converted"
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


if __name__ == '__main__':
    imgs_path = r'E:\pidinet-master\custom'
    checkpoints_path = r'E:\pidinet-master\trained_models\table5_pidinet.pth'
    save_path = r'E:\pidinet-master\result'
    img_results_folder = os.path.join(save_path, 'eval_results/imgs_epoch_020') # 白底黑边
    gt_path = r'E:\Datasets\BSDS_datasets_\BSDS500\data\GT_convert_0\train' # 白底黑边


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
            print(f'precision:{precision}')
            print(f'recall:{recall}')
            print(f'f1_score:{f1_score}')
        else:
            print('gt为None')



    
