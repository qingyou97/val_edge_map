import os

# A文件夹路径
base_dir = 'A'

# 将在每个子文件夹下创建的四个新文件夹名称
new_folders = ['test_gt', 'test_images', 'train_gt', 'train_images']

# 遍历A文件夹下的所有子文件夹
for subdir in next(os.walk(base_dir))[1]:
    subdir_path = os.path.join(base_dir, subdir)
    for folder in new_folders:
        new_folder_path = os.path.join(subdir_path, folder)
        os.makedirs(new_folder_path, exist_ok=True)
