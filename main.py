import numpy as np
from skimage.io import imread, imsave
from skimage.transform import resize

def resize_binary_image(image_path, output_path, scale=0.5):
    # 读取图像
    image = imread(image_path, as_gray=True)
    
    # 获取新大小
    new_height = int(image.shape[0] * scale)
    new_width = int(image.shape[1] * scale)
    
    # 调整图像大小
    resized_image = resize(image, (new_height, new_width), order=0, preserve_range=True, anti_aliasing=False)
    
    # 保存调整大小后的图像
    imsave(output_path, resized_image.astype(np.uint8))

# 例: 使用该函数
resize_binary_image('input_binary_image.png', 'output_resized_image.png')
