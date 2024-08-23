import os

# 文件夹路径
folder_path = 'A'

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 检查文件后缀是否为.jpeg
    if filename.endswith(".jpeg"):
        # 定义旧文件路径
        old_filepath = os.path.join(folder_path, filename)
        # 创建新的文件路径并更改后缀名为.jpg
        new_filepath = os.path.join(folder_path, filename[:-5] + ".jpg")
        # 重命名文件
        os.rename(old_filepath, new_filepath)
        
print("重命名完成")
