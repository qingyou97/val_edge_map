# 指定的起始和结束数字
start_num = 12
end_num = 31

# 获取主文件夹下的所有子文件夹
subfolders = [os.path.join(main_folder, subfolder) for subfolder in os.listdir(main_folder) if os.path.isdir(os.path.join(main_folder, subfolder))]

for folder in subfolders:
    print(f"Processing folder: {folder}")
    # 遍历子文件夹中的所有文件
    for filename in os.listdir(folder):
        print(f"Checking file: {filename}")
        # 使用正则表达式匹配文件名开头的数字
        match = re.match(r'^(\\d+)_.*\\.png$', filename)
        if match:
            number = int(match.group(1))
            print(f"Found number: {number}")
            # 删除不在 12 到 31 范围内的文件
            if number < start_num or number > end_num:
                file_path = os.path.join(folder, filename)
                try:
                    os.remove(file_path)
                    print(f"Deleted {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
        else:
            print(f"No match for file: {filename}")
