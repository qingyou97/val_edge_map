import os

# 需要创建的文件夹名字列表
folders = [
    "bottle", "cable", "capsule", "carpet", "grid", "hazelnut", "leather",
    "metal_nut", "pill", "screw", "tile", "toothbrush", "transistor", "wood", "zipper"
]

# A目录的路径
base_path = 'A'

# 确保A目录存在
os.makedirs(base_path, exist_ok=True)

# 创建文件夹
for folder in folders:
    os.makedirs(os.path.join(base_path, folder), exist_ok=True)
