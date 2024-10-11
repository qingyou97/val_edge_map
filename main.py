import cv2
import numpy as np


def get_brightness(image, thresh):
    height, width = image.shape

    # 创建一个新的图像副本用于标记
    # marked_image = image.copy()
    marked_image = np.zeros_like(image)

    # 遍历每个像素 寻找左边像素更亮的像素
    for y in range(height):
        for x in range(1, width // 2):  # 从1开始以确保有左边的像素
            diff = np.subtract(image[y, x - 1], image[y, x], dtype=np.int32, casting='unsafe')
            if diff >= thresh:
                marked_image[y, x] = 255  # 将符合条件的像素标记为白色

    # 遍历每个像素 寻找右边像素更亮的像素
    for y in range(height):
        for x in range(width // 2, width):
            diff = np.subtract(image[y, x], image[y, x - 1], dtype=np.int32, casting='unsafe')
            if diff >= thresh:
                marked_image[y, x] = 255  # 将符合条件的像素标记为白色

    # 保存标记后的图片
    # cv2.imwrite('marked_image.png', marked_image)
    # print("标记后的图片已保存为 'marked_image.png'")
    return marked_image


def make_intersection(image1, image2, path):
    _, image2 = cv2.threshold(image2, 127, 255, cv2.THRESH_BINARY)

    # 确保图像尺寸相同
    assert image1.shape == image2.shape, "两张图像的尺寸不同"

    # 使用逻辑和操作找出对应像素都是白色的区域
    result = cv2.bitwise_and(image1, image2)

    # 将结果与原图的逻辑和进行比较，看哪些像素实际上都是白色，生成最终的结果图像
    white_pixels = np.where(result == 255, 255, 0).astype(np.uint8)

    # 保存结果图像
    cv2.imwrite(path, white_pixels)

    print(f"结果已保存为{path}")


if __name__ == '__main__':
    ori_img = r'D:\Projects\edge_detection\rule_based\cast_def_0_2.jpeg'  # 原图
    save_path = 'result.png'  # 保存的结果图
    thresh = 10  # 亮度差异

    # 读取原图，获得亮度
    image = cv2.imread(ori_img, cv2.IMREAD_GRAYSCALE)
    # filter后的黑白图片
    image2 = cv2.imread('cast_def_0_2.png', cv2.IMREAD_GRAYSCALE)

    # 获取相邻像素更亮的像素或者更暗的像素
    pattern = get_brightness(image, thresh)

    make_intersection(pattern, image2, save_path)
