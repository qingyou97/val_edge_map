def copy_folder_with_self(src, dst):
    # 获取A文件夹的名称
    folder_name = os.path.basename(src.rstrip('/\\\\'))
    dst_path = os.path.join(dst, folder_name)
    
    # 使用shutil.copytree将A文件夹及其所有内容复制到B文件夹
    shutil.copytree(src, dst_path, dirs_exist_ok=True)
