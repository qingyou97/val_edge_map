from PIL import Image

def process_image(input_path, output_path):
    image = Image.open(input_path).convert("RGBA")
    data = image.getdata()

    new_data = []
    for item in data:
        # 检查白色点 (255, 255, 255, 255)
        if item[:3] == (255, 255, 255):
            # 变为 (253, 231, 36, 255)
            new_data.append((253, 231, 36, 255))
        else:
            # 其余点变为 (68, 1, 84, 255)
            new_data.append((68, 1, 84, 255))

    image.putdata(new_data)
    image.save(output_path)

# 调用示例
input_path = 'input_image.png'  # 输入图像路径
output_path = 'output_image.png'  # 输出图像路径
process_image(input_path, output_path)
