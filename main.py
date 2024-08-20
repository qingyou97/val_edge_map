from PIL import Image

# 打开图像文件
input_path = "path/to/your/image.jpg"  # 替换为你的图像路径
output_path = "path/to/save/scaled_image.jpg"  # 替换为你想保存图像的路径

# 使用最近邻插值调整图像大小，将图像缩放到512x512
with Image.open(input_path) as img:
    img_resized = img.resize((512, 512), Image.NEAREST)
    img_resized.save(output_path)
    
print(f"图像已缩放并保存至: {output_path}")
