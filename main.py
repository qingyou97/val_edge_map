from PIL import Image

def resize_binarized_png(image_path: str, output_path: str, scale: float = 0.5):
    # 打开图像文件
    image = Image.open(image_path)
    
    # 获取原始图像的尺寸
    original_width, original_height = image.size
    
    # 计算新尺寸
    new_width = int(original_width * scale)
    new_height = int(original_height * scale)
    
    # 使用最近邻插值法进行缩放
    resized_image = image.resize((new_width, new_height), Image.NEAREST)
    
    # 保存缩放后的图像
    resized_image.save(output_path)
    
# 使用示例
resize_binarized_png('input_image.png', 'resized_image.png')
