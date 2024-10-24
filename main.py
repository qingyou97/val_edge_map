from PIL import Image

def find_pixels_with_rgba(image_path, target_rgba):
    # 打开图像
    img = Image.open(image_path).convert('RGBA')
    pixels = img.load()
    width, height = img.size
    
    # 结果列表
    matching_points = []

    # 遍历图像中所有像素
    for x in range(width):
        for y in range(height):
            if pixels[x, y] == target_rgba:
                matching_points.append((x, y))

    return matching_points

# 示范
image_path = 'path_to_your_image.png'
target_rgba = (253, 231, 36, 255)
matching_points = find_pixels_with_rgba(image_path, target_rgba)
print(matching_points)
