from PIL import Image

def find_non_matching_color_coordinates(image_path, target_color):
    # 打开图像
    img = Image.open(image_path)
    
    # 确保这是一个RGBA图像
    img = img.convert("RGBA")
    
    # 获取图像的宽高
    width, height = img.size
    
    # 获取图像的数据
    pixels = img.load()
    
    # 存储不匹配目标颜色的像素的坐标
    non_matching_coords = set()
    
    # 遍历每个像素，检查是否与目标颜色不同
    for y in range(height):
        for x in range(width):
            if pixels[x, y] != target_color:
                non_matching_coords.add((x, y))
    
    return non_matching_coords

# 示例使用
image_path = os.path.join(ai_result_folder, filename.replace('original', 'ai_result'))
target_color = (253, 231, 36, 255)
non_matching_coordinates = find_non_matching_color_coordinates(image_path, target_color)

for coord in non_matching_coordinates:
    print(coord)
