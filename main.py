import os

def rename_files(folder_path):
    for filename in os.listdir(folder_path):
        new_filename = filename.replace('_mask', '')
        if new_filename != filename:
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            print(f'Renamed: {filename} -> {new_filename}')
        else:
            print(f'Skipped: {filename}')
    
folder_path = 'A文件夹的路径'  # 替换为实际文件夹路径
rename_files(folder_path)
