file_name = os.path.basename(file_path)  # 获取最后的文件名，即 "14_2.png"
prefix = os.path.splitext(file_name)[0]  # 去掉文件扩展名，只留下前缀，即 "14_2"
保持图像中的细边缘而防止它们消失，你可能更适合使用最近邻插值。虽然它可能会带来某些锯齿效应，但它能够更好地保留细边缘。
