import os

folder_path = 'your_folder_path'  # 替换为你的文件夹路径

for filename in os.listdir(folder_path):
    if filename.lower().endswith('.jpeg'):
        new_filename = filename.rsplit('.', 1)[0] + '.jpg'
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        print(f'Renamed: {filename} -> {new_filename}')
