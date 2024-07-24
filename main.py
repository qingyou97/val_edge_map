import os

def check_folders(parent_folder):
    for folder_name in os.listdir(parent_folder):
        folder_path = os.path.join(parent_folder, folder_name)
        if os.path.isdir(folder_path):
            test_gt_path = os.path.join(folder_path, 'test_gt')
            if os.path.exists(test_gt_path) and os.path.isdir(test_gt_path):
                image_files = [f for f in os.listdir(test_gt_path) if os.path.isfile(os.path.join(test_gt_path, f))]
                if len(image_files) <= 1:
                    print(folder_name)

# 使用示例
parent_folder = 'A'  # 替换为你的父文件夹路径
check_folders(parent_folder)
