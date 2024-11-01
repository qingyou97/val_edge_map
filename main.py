def copy_folders_to_new_directory(source_dirs, destination_dir):
    # 创建目标文件夹，如果不存在
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    for folder in source_dirs:
        # 获取文件夹名称
        folder_name = os.path.basename(folder)
        # 目标文件夹路径
        destination_folder = os.path.join(destination_dir, folder_name)
        # 复制文件夹
        shutil.copytree(folder, destination_folder)

source_dirs = ['/path/to/first/folder', '/path/to/second/folder', '/path/to/third/folder']
destination_dir = '/path/to/new/directory'

copy_folders_to_new_directory(source_dirs, destination_dir)
