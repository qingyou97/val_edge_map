import numpy as np
import scipy.ndimage
import imageio

def zoom_image(image_path, zoom_factor=0.5):
    # 读取图像
    image = imageio.imread(image_path)
    
    # 使用zoom函数进行最近邻插值
    zoomed_image = scipy.ndimage.zoom(image, zoom=(zoom_factor, zoom_factor, 1), order=0, mode='nearest')
    
    return zoomed_image

# 示例用法：
resized_image = zoom_image('path_to_image.jpg')
# 可以根据需要保存或展示resized_image
imageio.imwrite('resized_image.jpg', resized_image)
