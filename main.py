import cv2
import numpy as np

def process_image(image):
    # 获得图像的高度和宽度
    height, width = image.shape

    # 复制一份图像用于操作
    output = image.copy()

    # 检查每个白色像素(像素值为255)，看看它是否为单独的像素点，并进行处理
    for y in range(1, height-1):
        for x in range(1, width-1):
            if image[y, x] == 255:
                # 检查周围8个像素
                neighbors = image[y-1:y+2, x-1:x+2]
                count_white = np.sum(neighbors == 255) - 1 # 排除中心点

                if count_white == 0:
                    # 该像素是单独的，检查两侧有无白色像素线段，来决定如何处理
                    if image[y, x-1] == 255 or image[y, x+1] == 255:
                        output[y, x] = 0  # 如果在水平线段中，移除这个像素
                    elif image[y-1, x] == 255 or image[y+1, x] == 255:
                        output[y, x] = 0  # 如果在垂直线段中，移除这个像素
                    else:
                        for dy in [-1, 0, 1]:
                            for dx in [-1, 0, 1]:
                                if (dx == 0 and dy == 0) or (x + 2 * dx < 0) or (x + 2 * dx >= width) or (y + 2 * dy < 0) or (y + 2 * dy >= height):
                                    continue
                                if image[y + dy, x + dx] == 255 and image[y - dy, x - dx] == 255:
                                    output[y, x] = 0
                                    output[y + dx, x + dy] = 255
                                    break

    return output


# 加载黑白图像（图像的路径自己改一下）
image_path = 'path_to_your_image.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# 处理图像
processed_image = process_image(image)

# 保存结果图像
output_path = 'processed_image.png'
cv2.imwrite(output_path, processed_image)

# 展示结果
cv2.imshow('Processed Image', processed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
