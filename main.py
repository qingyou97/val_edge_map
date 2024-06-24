import os
from PIL import Image

# 定义A文件夹和B文件夹的路径
a_folder = 'path/to/A_folder'
b_folder = 'path/to/B_folder'

# 确保B文件夹存在，如果不存在则创建
if not os.path.exists(b_folder):
    os.makedirs(b_folder)

# 遍历A文件夹内的所有文件
for filename in os.listdir(a_folder):
    if filename.endswith('.png'):
        # 打开图像
        img = Image.open(os.path.join(a_folder, filename))

        # 将图像转为灰度图（防止出现带颜色的结果）
        img = img.convert('L')

        # 反转图像的像素值（黑色变白色，白色变黑色）
        img_inverted = Image.eval(img, lambda x: 255 - x)
        
        # 将修改后的图像保存到B文件夹
        save_path = os.path.join(b_folder, filename)
        img_inverted.save(save_path)

print("图像已经转换并保存到B文件夹")
