import os

# 设定文件夹路径
folder_path = '你的文件夹路径'

# 获取文件夹内的所有文件
files = os.listdir(folder_path)

# 遍历文件
for filename in files:
    if filename.lower().endswith('.jpeg'):
        # 构建旧文件路径
        old_filepath = os.path.join(folder_path, filename)
        # 构建新文件路径
        new_filepath = os.path.join(folder_path, filename[:-5] + '.jpg')
        # 重命名文件
        os.rename(old_filepath, new_filepath)

print("所有jpeg图像已成功改为jpg图像!")
