import shutil
import os

def delete_all_contents(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.unlink(item_path)  # 删除文件或符号链接
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)  # 删除目录及其所有内容

# 示例用法
directory_to_delete = "/path/to/your/directory"
delete_all_contents(directory_to_delete)
