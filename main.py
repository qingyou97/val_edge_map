import os
from PIL import Image

def convert_to_black_white(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            image_path = os.path.join(directory, filename)
            img = Image.open(image_path).convert('L')  # 转化为灰度图
            bw = img.point(lambda x: 0 if x < 128 else 255, '1')  # 转化为黑白图
            bw.save(image_path)  # 覆盖原图/或使用新的文件名保存

folder_path = '你的文件夹路径' 
convert_to_black_white(folder_path)
