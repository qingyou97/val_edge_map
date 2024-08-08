import os
from PIL import Image

# 指定文件夹路径
folder_path = '你的文件夹路径'

# 遍历文件夹中的每个文件
for filename in os.listdir(folder_path):
    # 检查文件是否是jpg文件
    if filename.endswith('.jpg'):
        # 构建完整文件路径
        file_path = os.path.join(folder_path, filename)
        
        # 打开图像
        with Image.open(file_path) as img:
            # 构建新的文件名，以jpeg结尾
            new_filename = filename[:-4] + '.jpeg'
            new_file_path = os.path.join(folder_path, new_filename)
            
            # 保存为jpeg格式
            img.save(new_file_path, 'JPEG')
            
        # 删除旧的jpg文件
        os.remove(file_path)

print("所有 jpg 图像已转换为 jpeg 格式。")
