import os
import cv2


def make_edge_mask(seg_mask_path, edge_mask_path):
    if not os.path.exists(edge_mask_path, ):
        os.makedirs(edge_mask_path,exist_ok=True)

    seg_mask_list = os.listdir(seg_mask_path)

    for mask in seg_mask_list:
        mask_path = os.path.join(seg_mask_path, mask)

        # 读取mask图像
        mask = cv2.imread(r'E:\seg2edge\20160222_080933_721_1921.png', 0)  # 灰度模式读取

        # 使用Canny算法提取边缘
        edges = cv2.Canny(mask, 100, 200)

        # 保存或显示边缘图像
        cv2.imwrite(os.path.join(edge_mask_path, mask), edges)
        # cv2.imshow('Edges', edges)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()



if __name__ == '__main__':
    seg_mask_path = '' # 分割mask路径
    edge_mask_path = '' # 边缘mask路径
    make_edge_mask(seg_mask_path, edge_mask_path)
