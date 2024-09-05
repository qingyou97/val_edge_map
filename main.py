# 获取并排序文件夹名，并过滤掉不包含'_result'的文件夹
folder_names = [name for name in os.listdir(folder_path) if '_result' in name]
folder_names.sort(key=natural_sort_key)
