def update_cfg(filename, new_data_root, new_data_lst):
    # 读取文件内容
    with open(filename, 'r', encoding='utf-8') as file:
        file_content = file.read()
    
    # 使用正则表达式替换指定内容
    file_content = re.sub(
        r"('data_root':\\s*')[^']*(')",
        r"\\1" + new_data_root + r"\\2",
        file_content
    )
    file_content = re.sub(
        r"('data_lst':\\s*')[^']*(')",
        r"\\1" + new_data_lst + r"\\2",
        file_content
    )
    
    # 保存回原文件
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(file_content)
