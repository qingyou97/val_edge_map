def write_image_paths_to_txt(folder_path, output_file):
    with open(output_file, 'w') as file:
        for root, dirs, files in os.walk(folder_path):
            for name in files:
                if name.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                    file.write(os.path.join(root, name) + '\
')

# 使用示例
folder_path = 'A'  # 你的文件夹路径
output_file = 'output.txt'  # 输出的txt文件名
write_image_paths_to_txt(folder_path, output_file)
