import scipy.ndimage
import imageio

def resize_image_half_nearest_neighbor(input_path, output_path):
    # 读取图像
    image = imageio.imread(input_path)

    # 缩放图像
    scale_y, scale_x = 0.5, 0.5
    zoomed_image = scipy.ndimage.zoom(image, (scale_y, scale_x, 1), order=0)

    # 保存图像
    imageio.imwrite(output_path, zoomed_image)

# 调用函数示例
resize_image_half_nearest_neighbor('input_image_path.jpg', 'output_image_path.jpg')
