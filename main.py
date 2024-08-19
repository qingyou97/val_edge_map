import os
import glob
from PIL import Image

# 获取所有子文件夹的路径
parent_folder = 'E:\\\\test'
folders = [f.path for f in os.scandir(parent_folder) if f.is_dir()]
destination_dir = r'E:\oneimage/'

# 确保读取到的文件夹数量正确
if len(folders) != 576:
    print("文件夹数量不足576个，实际数量:", len(folders))
else:
    print("读取到文件夹数量:", len(folders))
    # 循环读取这些文件夹
    for folder in folders:
        print(f'正在读取文件夹: {folder}')
        last_layer = os.path.basename(folder)
        print(f'文件夹: {last_layer}')

        # 获取所有图像文件
        for filename in os.listdir(folder):
            if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                img_path = os.path.join(folder, filename)
                img = Image.open(img_path)

                # 新的文件名
                new_filename = f'{last_layer}_{filename}'
                new_img_path = os.path.join(destination_dir, new_filename)

                # 保存图像
                img.save(new_img_path)

        print("所有图像已处理并保存到新文件夹。")
