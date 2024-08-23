# 确保目标文件夹
os.makedirs(target_folder, exist_ok=True)

# 遍历每个源文件夹
for folder in source_folders:
    source_image_folder = os.path.join(folder, 'image_512')
    # 如果源文件夹存在
    if os.path.exists(source_image_folder):
        # 遍历每个文件
        for file_name in os.listdir(source_image_folder):
            source_file = os.path.join(source_image_folder, file_name)
            # 如果是文件
            if os.path.isfile(source_file):
                # 新文件名
                new_file_name = f"{folder}_{file_name}"
                target_file = os.path.join(target_folder, new_file_name)
                try:
                    # 复制文件到目标文件夹
                    shutil.copy2(source_file, target_file)
                    print(f"复制 {source_file} 到 {target_file}")
                except Exception as e:
                    print(f"复制 {source_file} 到 {target_file} 失败: {e}")
    else:
        print(f"源文件夹 {source_image_folder} 不存在")
