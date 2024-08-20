import scipy.ndimage
import imageio

def resize_image_half_nearest_neighbor(input_path, output_path):
    # 读取图像
    image = imageio.imread(input_path)

    # 确定缩放比例
    scale_y, scale_x = 0.5, 0.5
    zoom_factors = (scale_y, scale_x)

    # 缩放图像
    zoomed_image = scipy.ndimage.zoom(image, zoom_factors, order=0)

    # 保存图像
    imageio.imwrite(output_path, zoomed_image)

# 调用函数示例
resize_image_half_nearest_neighbor('input_image_path.png', 'output_image_path.png')
