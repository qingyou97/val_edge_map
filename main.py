import os

# 文件夹路径
folder_path = 'A文件夹路径'

# 获取所有文件夹名
folder_names = sorted(os.listdir(folder_path))

# 用于记录配对的字典
paired_folders = {}

# 遍历文件夹名并按照配对关系进行匹配
for name in folder_names:
    key = name.rsplit('_', 1)[0]
    if key in paired_folders:
        paired_folders[key].append(name)
    else:
        paired_folders[key] = [name]

# 打印配对结果
for pair in paired_folders.values():
    if len(pair) == 2:
        print(pair[0], '和', pair[1], '是一对')
