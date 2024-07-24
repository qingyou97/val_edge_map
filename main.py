import os

# 主目录A和目标目录Z
main_dir = 'A'
target_dir = 'Z'

# 需要依次读取的文件夹名称
folders = ["bottle", "cable", "capsule", "carpet", "grid", "hazelnut", "leather", "metal_nut", "pill", "screw", "tile", "toothbrush", "transistor", "wood", "zipper"]

# 忽略txt文件，遍历主要文件夹
for folder in folders:
    # Ground truth目录
    ground_truth_dir = os.path.join(main_dir, folder, 'ground_truth')
    
    if os.path.exists(ground_truth_dir):
        # 获取ground_truth目录下的所有子文件夹
        subfolders = [name for name in os.listdir(ground_truth_dir) if os.path.isdir(os.path.join(ground_truth_dir, name))]
        
        for subfolder in subfolders:
            # 新文件夹名称
            new_folder_name = f"{folder}_{subfolder}"
            new_folder_path = os.path.join(target_dir, new_folder_name)
            
            # 创建新文件夹
            os.makedirs(new_folder_path, exist_ok=True)
