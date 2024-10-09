import os
from PIL import Image, ImageChops

# 定义文件夹路径
original_folder = 'A文件夹'
ai_result_folder = 'B文件夹'
output_folder = '结果文件夹'

#确保输出文件夹存在
os.makedirs(output_folder, exist_ok=True)

# RGB 文件中的标签颜色
label_color = (253, 231, 36, 255)

#获取所有文件名
original_files = sorted([f for f in os.listdir(original_folder) if f.endswith('.png')])
ai_result_files = sorted([f for f in os.listdir(ai_result_folder) if f.endswith('.png')])

for original_file, ai_result_file in zip(original_files, ai_result_files):
    original_path = os.path.join(original_folder, original_file)
    ai_result_path = os.path.join(ai_result_folder, ai_result_file)
    
    original_image = Image.open(original_path).convert('RGBA')
    ai_result_image = Image.open(ai_result_path).convert('RGBA')
    
    # 新图像，用来存储修改后的结果
    result_image = Image.new('RGBA', original_image.size)
    
    original_pixels = original_image.load()
    ai_result_pixels = ai_result_image.load()
    result_pixels = result_image.load()
    
    for y in range(original_image.height):
        for x in range(original_image.width):
            if ai_result_pixels[x, y] == label_color:
                result_pixels[x, y] = original_pixels[x, y]
            else:
                result_pixels[x, y] = (0, 0, 0, 255)
    
    # 保存结果文件
    result_image.save(os.path.join(output_folder, original_file.replace('_original', '_filtered')))

print("操作完成，每对图像已处理并保存。")
