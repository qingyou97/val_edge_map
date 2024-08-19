from PIL import Image
import os

# 定义原始文件夹和目标文件夹路径
folders = ["A", "B"]
target_size = (512, 512)

for folder in folders:
    new_folder = folder + "512"
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    
    for filename in os.listdir(folder):
        if filename.endswith((".jpg", ".png", ".jpeg")):  # 根据需要调整支持的文件扩展名
            img_path = os.path.join(folder, filename)
            img = Image.open(img_path)
            img_resized = img.resize(target_size)
            new_img_path = os.path.join(new_folder, filename)
            img_resized.save(new_img_path)

print("图像调整大小完成并保存到新文件夹。")
