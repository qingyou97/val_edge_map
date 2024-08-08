def copy_tree(src, dst):
    # 如果B文件夹不存在，则创建
    if not os.path.exists(dst):
        os.makedirs(dst)
    
    # 使用shutil.copytree将A文件夹及其所有内容复制到B文件夹
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
        else:
            shutil.copy2(src_path, dst_path)
