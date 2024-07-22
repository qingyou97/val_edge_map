import os

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"文件夹 '{folder_path}' 已被创建。")
    else:
        print(f"文件夹 '{folder_path}' 已经存在。")
