import os
from PIL import Image
import collections

def calculate_image_resolutions(folder_path):
    # 保存每个分辨率的图像数量
    resolution_counts = collections.Counter()
    
    # 初始化总宽度和总高度
    total_width, total_height = 0, 0
    image_count = 0
    
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
            try:
                # 获取图像的分辨率
                with Image.open(os.path.join(folder_path, filename)) as img:
                    width, height = img.size
                    resolution_counts[(width, height)] += 1
                    total_width += width
                    total_height += height
                    image_count += 1
            except Exception as e:
                print(f"Error processing image {filename}: {e}")

    if image_count == 0:
        print("无法计算平均分辨率，因为文件夹中没有有效图像。")
        return

    # 计算平均分辨率
    average_width = total_width / image_count
    average_height = total_height / image_count
    
    # 输出结果
    print(f"平均分辨率: {average_width} x {average_height}")
    print("每种分辨率下的图像数量:")
    for resolution, count in resolution_counts.items():
        print(f"{resolution[0]} x {resolution[1]}: {count} 张")

# 示例用法
folder_path = 'path/to/your/image/folder'
calculate_image_resolutions(folder_path)
