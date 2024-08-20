file_name = os.path.basename(file_path)  # 获取最后的文件名，即 "14_2.png"
prefix = os.path.splitext(file_name)[0]  # 去掉文件扩展名，只留下前缀，即 "14_2"
