import os
import shutil
import stat

# A 和 B 文件夹路径
folder_A = '/path/to/A'
folder_B = '/path/to/B'

def set_rw_permissions(path):
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | 
                  stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP |
                  stat.S_IROTH | stat.S_IWOTH | stat.S_IXOTH)

for root, dirs, files in os.walk(folder_A):
    for directory in dirs:
        # Parse the directory name under A folder
        parts = directory.split('_', 1)

        if len(parts) != 2:
            continue # Skip if the name doesn't follow the expected pattern

        first_part, second_part = parts
        source_dir = os.path.join(folder_B, first_part, 'test', second_part)

        if os.path.exists(source_dir):
            dest_dir = os.path.join(root, directory, 'test_images')
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            # Copy all files from source_dir to dest_dir
            for item in os.listdir(source_dir):
                s = os.path.join(source_dir, item)
                d = os.path.join(dest_dir, item)
                
                if os.path.isfile(s):
                    shutil.copy2(s, d)
                    set_rw_permissions(d)

print("文件复制完成。")
