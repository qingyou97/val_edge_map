import cv2
import numpy as np

def mark_points_with_color(image_a_path, image_b_path, target_rgba, output_path, mark_color=[255, 0, 0, 255]):
    """
    在B图上用指定颜色标注A图中指定RGBA值的点。

    :param image_a_path: A图的路径
    :param image_b_path: B图的路径
    :param target_rgba: 需要查找的RGBA值，例如[253, 231, 36, 255]
    :param output_path: 标注后的B图保存路径
    :param mark_color: 标注颜色，默认为红色[255, 0, 0, 255]
    """
    # 读取A图和B图
    image_a = cv2.imread(image_a_path, cv2.IMREAD_UNCHANGED)
    image_b = cv2.imread(image_b_path, cv2.IMREAD_UNCHANGED)

    if image_a is None or image_b is None:
        raise FileNotFoundError("无法读取图像文件，请检查路径是否正确。")

    if image_a.shape != image_b.shape:
        raise ValueError("A图和B图的大小不一致。")

    # 找到A图中target_rgba点的位置
    mask = np.all(image_a == target_rgba, axis=-1)
    indices = np.where(mask)

    # 在B图上用指定颜色标注这些点
    for y, x in zip(*indices):
        image_b[y, x] = mark_color

    # 保存标注后的B图
    cv2.imwrite(output_path, image_b)
    print(f"标注完成并保存为'{output_path}'")

# 示例调用
mark_points_with_color('A.png', 'B.png', [253, 231, 36, 255], 'B_annotated.png')
