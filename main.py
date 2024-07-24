import os

def rename_images(base_folder):
    # 遍历A文件夹下的所有子文件夹
    for root, subdirs, files in os.walk(base_folder):
        # 检查是否是"test_gt"文件夹
        if os.path.basename(root) == "test_gt":
            for file in files:
                if "_mask" in file:  # 检查文件名是否包含"_mask"
                    src = os.path.join(root, file)
                    dst = os.path.join(root, file.replace('_mask', ''))
                    os.rename(src, dst)
                    print(f'Renamed: {src} -> {dst}')

# 替换为你的文件夹路径
base_folder = 'A文件夹路径'
rename_images(base_folder)["bottle", "cable", "capsule", "carpet", "grid", "hazelnut", "leather", "metal_nut", "pill", "screw", "tile", "toothbrush", "transistor", "wood", "zipper"]
