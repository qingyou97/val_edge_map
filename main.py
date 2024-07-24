import os
import shutil

# 定义A文件夹和B文件夹路径
A_folder_path = "path/to/A_folder"
B_folder_path = "path/to/B_folder"

# 定义函数来遍历文件夹中的所有文件夹和子文件夹
for root, dirs, files in os.walk(A_folder_path):
    for dir_name in dirs:
        # 解析文件夹名称
        item_name, sub_name = dir_name.rsplit('_', 1)
        
        # 分别获取A文件夹和B文件夹路径
        src_folder = os.path.join(B_folder_path, item_name, "ground_truth", sub_name)
        dest_folder = os.path.join(root, dir_name, "test_gt")
        
        # 确保目标文件夹存在，如果不存在则创建
        os.makedirs(dest_folder, exist_ok=True)

        # 获取源文件夹中的所有图像文件并复制到目标文件夹
        if os.path.exists(src_folder):
            for img_file in os.listdir(src_folder):
                src_file_path = os.path.join(src_folder, img_file)
                dest_file_path = os.path.join(dest_folder, img_file)
                
                if os.path.isfile(src_file_path):
                    shutil.copy(src_file_path, dest_file_path)

    # 因为只需要在第一层文件夹执行（内层递归不会改变Already_in的数量）
    break

print("完成人工分类操作")
