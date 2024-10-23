# 读取图像并提取红色点的坐标
def extract_red_points(image_path):
    # 读取图片
    image = cv2.imread(image_path)
    # 转换为RGB颜色空间
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # 定义红色的RGB值
    red_color = np.array([255, 0, 0])
    # 找到所有红色点的坐标
    red_points = np.where(np.all(rgb_image == red_color, axis=-1))
    # 将坐标转换为列表形式
    red_points_list = list(zip(red_points[1], red_points[0]))  # 注意顺序是(x, y)
    return red_points_list
