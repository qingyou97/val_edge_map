import os

# 定义文件夹路径
base_path = 'A'  # 假设你的文件夹路径是A
test_gt = os.path.join(base_path, 'test_gt')
test_images = os.path.join(base_path, 'test_images')
train_gt = os.path.join(base_path, 'train_gt')
train_images = os.path.join(base_path, 'train_images')

# 临时重命名为了防止覆盖
temp_test_gt = os.path.join(base_path, 'temp_test_gt')
temp_test_images = os.path.join(base_path, 'temp_test_images')

os.rename(test_gt, temp_test_gt)
os.rename(test_images, temp_test_images)

# 相应地重命名文件夹
os.rename(train_gt, os.path.join(base_path, 'test_gt'))
os.rename(train_images, os.path.join(base_path, 'test_images'))

# 将临时命名的文件夹重新命名为需要的名称
os.rename(temp_test_gt, os.path.join(base_path, 'train_gt'))
os.rename(temp_test_images, os.path.join(base_path, 'train_images'))
