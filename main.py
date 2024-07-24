import os
import shutil
import stat

# 替换为你要清空的文件夹路径
folder_path = "A"

def remove_readonly(func, path, _):
    os.chmod(path, stat.S_IWRITE)
    func(path)

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        try:
            os.remove(file_path)
        except PermissionError:
            os.chmod(file_path, stat.S_IWRITE)
            os.remove(file_path)
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        try:
            shutil.rmtree(dir_path, onerror=remove_readonly)
            os.makedirs(dir_path)
        except PermissionError:
            os.chmod(dir_path, stat.S_IWRITE)
            shutil.rmtree(dir_path, onerror=remove_readonly)
            os.makedirs(dir_path)
