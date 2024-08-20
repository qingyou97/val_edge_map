import cv2  # OpenCV库

def resize_by_half(image):
    height, width = image.shape[:2]
    while height > 512 or width > 512:
        height //= 2
        width //= 2
        image = cv2.resize(image, (width, height), interpolation=cv2.INTER_NEAREST)
    # 最终的调整
    image = cv2.resize(image, (512, 512), interpolation=cv2.INTER_NEAREST)
    return image

if __name__ == "__main__":
    image_path = "path/to/your/image.jpg"  # 替换为图像路径
    image = cv2.imread(image_path)
    resized_image = resize_by_half(image)
    cv2.imwrite("resized_image.jpg", resized_image)
