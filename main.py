def is_white(image, point):
    """
    判断在给定图像的给定点是否为白色。
    """
    x, y = point
    if image[y, x] == 255:
        return True
    return False

def find_white_point(image_path, point1, point2):
    """
    在给定的黑白图像中查找两个点中哪个点为白色。
    """
    # 读取图像
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 确保图像为黑白图像
    if image is None:
        raise ValueError("Image not found or incorrect image format")

    if len(image.shape) != 2:
        raise ValueError("Input image is not grayscale")

    # 检查两个点
    if is_white(image, point1):
        return point1
    elif is_white(image, point2):
        return point2
    else:
        return None  # 如果没有一个点是白色的，则返回None

# 测试函数
point1 = (10, 20)
point2 = (30, 40)
image_path = 'path/to/your/bw_image.png'
result = find_white_point(image_path, point1, point2)
print("白色点是: ", result)
