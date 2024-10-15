import os

# A文件夹的路径
folder_A = 'path/to/your/A/folder'

# 遍历A文件夹中的每个子文件夹
for sub_folder in os.listdir(folder_A):
    sub_folder_path = os.path.join(folder_A, sub_folder)
    if os.path.isdir(sub_folder_path):
        # 遍历子文件夹中的每个文件
        for file_name in os.listdir(sub_folder_path):
            # 取出文件名前两位数字
            prefix = file_name[:2]
            try:
                # 转换为整数方便比较
                prefix_num = int(prefix)
                # 判断是否在12到31之间
                if prefix_num < 12 or prefix_num > 31:
                    file_path = os.path.join(sub_folder_path, file_name)
                    os.remove(file_path)  # 删除不符合条件的文件
                    print(f"Deleted: {file_path}")
            except ValueError:
                # 如果无法转换为整数，则跳过
                continue

print("完成!")
