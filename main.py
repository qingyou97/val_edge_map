import os

# 指定文件夹的路径
folder_path = './A'

# 遍历文件夹下的所有文件
for filename in os.listdir(folder_path):
    # 检查文件是否是图像文件，你可以根据需要调整文件类型
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # 构建新的文件名
        new_name = "_groove" + filename
        # 获取完整的文件路径
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)
        # 重命名文件
        os.rename(old_file, new_file)

print("文件重命名完成")
