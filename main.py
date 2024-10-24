import cv2
import numpy as np

def draw_hoops(hoops):
    # 创建一个224x224像素的黑色背景图像
    image = np.zeros((224, 224), dtype=np.uint8)
    
    # 遍历hoops
    for hoop in hoops:
        center = (hoop[0], hoop[1])
        outer_radius = hoop[2]
        inner_radius = None
        for item in hoops:
            if item[0] == center[0] and item[1] == center[1] and item[2] != outer_radius:
                inner_radius = item[2]
                break
        if inner_radius:
            # 计算mask
            mask = np.zeros((224, 224), dtype=np.uint8)
                
            cv2.circle(mask, center, outer_radius, 1, -1)
            cv2.circle(mask, center, inner_radius, 0, -1)

            # 将白色应用到掩膜内
            image[mask == 1] = 255

            cv2.circle(image, center, outer_radius, 255, 2)
            cv2.circle(image, center, inner_radius, 255, 2)

    # 显示图像
    cv2.imshow('Hoops', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage:
hoops = [[111, 110, 136], [111, 110, 98], [110, 111, 70], [110, 111, 65]]
draw_hoops(hoops)
