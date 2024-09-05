# 获取并排序文件夹名
folder_names = os.listdir(folder_path)
folder_names.sort(key=natural_sort_key)
