import cv2

def draw_red_rectangle(image_path, rect):
    # 读取图像
    image = cv2.imread(image_path)
    
    # 确保图像读取成功
    if image is None:
        print("Error: Could not read image.")
        return
    
    # 左上角坐标和右下角坐标
    top_left, bottom_right = rect
    
    # 画一个1像素的红色矩形边界
    cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 1)
    
    # 显示图像
    cv2.imshow('Image with Red Rectangle', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 使用例子：
draw_red_rectangle('input_image.jpg', [(18, 26), (61, 73)])
