## 按沿宽度对半分割
import os
import cv2

# 根目录
root = r'E:\test/'

# 创建相应的文件夹
os.makedirs(root + 'left_seg_image', exist_ok=True)
os.makedirs(root + 'right_seg_image', exist_ok=True)
os.makedirs(root + 'left_seg_gt', exist_ok=True)
os.makedirs(root + 'right_seg_gt', exist_ok=True)

# 获取图片文件名
ori_image_files = [f for f in os.listdir(root + 'ori_image') if f.endswith(('.png', '.jpg', '.jpeg'))]
ori_gt_files = [f for f in os.listdir(root + 'ori_gt') if f.endswith(('.png', '.jpg', '.jpeg'))]

for ori_image_file, ori_gt_file in zip(ori_image_files, ori_gt_files):
    # 读入原图和gt图像
    ori_image_path = os.path.join(root + 'ori_image', ori_image_file)
    ori_gt_path = os.path.join(root + 'ori_gt', ori_gt_file)

    image = cv2.imread(ori_image_path)
    gt_image = cv2.imread(ori_gt_path)

    # 原图像的宽高度
    height, width = image.shape[:2]

    if width % 2 != 0:
        print(f"Warning: {ori_image_file} 的宽度不是偶数，图像未处理。")
        continue

    mid = width // 2

    # 分割图像
    left_image = image[:, :mid]
    right_image = image[:, mid:]
    left_gt_image = gt_image[:, :mid]
    right_gt_image = gt_image[:, mid:]

    # 拼接存储路径
    left_image_path = os.path.join(root + 'left_seg_image', ori_image_file)
    right_image_path = os.path.join(root + 'right_seg_image', ori_image_file)
    left_gt_image_path = os.path.join(root + 'left_seg_gt', ori_gt_file)
    right_gt_image_path = os.path.join(root + 'right_seg_gt', ori_gt_file)

    # 保存图像
    cv2.imwrite(left_image_path, left_image)
    cv2.imwrite(right_image_path, right_image)
    cv2.imwrite(left_gt_image_path, left_gt_image)
    cv2.imwrite(right_gt_image_path, right_gt_image)

print("分割完成！")

## 旋转和裁剪
from concurrent.futures import ThreadPoolExecutor


def rotate_and_crop(image_folder, gt_folder):
    ori_image_folder = root + image_folder
    ori_gt_folder = root + gt_folder

    angles = [22.5, 45.0, 67.5, 90.0, 112.5, 135.0, 157.5, 180.0, 202.5, 225.0, 247.5, 270.0, 292.5, 315.0, 337.5]

    image_files = sorted(os.listdir(ori_image_folder))
    gt_files = sorted(os.listdir(ori_gt_folder))

    def find_largest_rotated_rect(w, h, angle):
        if w <= 0 or h <= 0:
            return 0, 0
        width_is_longer = w >= h
        side_long, side_short = (w, h) if width_is_longer else (h, w)
        sin_a, cos_a = abs(np.sin(angle)), abs(np.cos(angle))
        if side_short <= 2. * sin_a * cos_a * side_long or abs(sin_a - cos_a) < 1e-10:
            x = 0.5 * side_short
            wr = x / sin_a
            hr = x / cos_a
        else:
            cos_2a = cos_a * cos_a - sin_a * sin_a
            wr = (w * cos_a - h * sin_a) / cos_2a
            hr = (h * cos_a - w * sin_a) / cos_2a
        return int(wr), int(hr)

    def process_image(angle, img_file, gt_file):
        angle_str = f'{angle:.1f}'
        rotated_image_folder = root + f'{angle_str}_{image_folder}'
        rotated_gt_folder = root + f'{angle_str}_{gt_folder}'
        os.makedirs(rotated_image_folder, exist_ok=True)
        os.makedirs(rotated_gt_folder, exist_ok=True)

        img_path = os.path.join(ori_image_folder, img_file)
        gt_path = os.path.join(ori_gt_folder, gt_file)
        img = cv2.imread(img_path)
        gt = cv2.imread(gt_path, cv2.IMREAD_GRAYSCALE)

        (h, w) = img.shape[:2]
        center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        cos = np.abs(M[0, 0])
        sin = np.abs(M[0, 1])
        new_w = int((h * sin) + (w * cos))
        new_h = int((h * cos) + (w * sin))

        M[0, 2] += (new_w / 2) - center[0]
        M[1, 2] += (new_h / 2) - center[1]

        rotated_img = cv2.warpAffine(img, M, (new_w, new_h))
        rotated_gt = cv2.warpAffine(gt, M, (new_w, new_h))
        wr, hr = find_largest_rotated_rect(w, h, np.radians(angle))
        x_center, y_center = int(new_w / 2), int(new_h / 2)
        cropped_rotated_img = rotated_img[y_center - hr // 2: y_center + hr // 2,
                              x_center - wr // 2: x_center + wr // 2]
        cropped_rotated_gt = rotated_gt[y_center - hr // 2: y_center + hr // 2, x_center - wr // 2: x_center + wr // 2]

        rotated_img_path = os.path.join(rotated_image_folder, f'{img_file}')
        rotated_gt_path = os.path.join(rotated_gt_folder, f'{gt_file}')
        cv2.imwrite(rotated_img_path, cropped_rotated_img)
        cv2.imwrite(rotated_gt_path, cropped_rotated_gt)

    for angle in angles:
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(process_image, angle, img_file, gt_file)
                       for img_file, gt_file in zip(image_files, gt_files)]

            for future in futures:
                future.result()

    print(f"{image_folder}旋转和裁剪处理完成！")


rotate_and_crop('left_seg_image', 'left_seg_gt')
rotate_and_crop('ori_image', 'ori_gt')
rotate_and_crop('right_seg_image', 'right_seg_gt')

# 水平翻转
import os
from PIL import Image

# 收集所有子文件夹
subdirs = [os.path.join(root, subdir) for subdir in os.listdir(root) if os.path.isdir(os.path.join(root, subdir))]

# 遍历每个子文件夹和图像
for original_subdir_path in subdirs:
    subdir_name = os.path.basename(original_subdir_path)
    new_subdir_name = "overturn_" + subdir_name
    new_subdir_path = os.path.join(root, new_subdir_name)
    os.makedirs(new_subdir_path, exist_ok=True)

    for image_name in os.listdir(original_subdir_path):
        image_path = os.path.join(original_subdir_path, image_name)
        if os.path.isfile(image_path):
            with Image.open(image_path) as img:
                flipped_img = img.transpose(method=Image.FLIP_LEFT_RIGHT)
                flipped_img.save(os.path.join(new_subdir_path, image_name))
    print(f'{new_subdir_path}翻转完成')

print("所有图像翻转完成并保存。")

# 伽马校正
import cv2
import os
import numpy as np
import shutil


def adjust_gamma(image, gamma):
    inv_gamma = 1.0 / gamma
    table = np.array([(i / 255.0) ** inv_gamma * 255 for i in range(256)]).astype("uint8")
    return cv2.LUT(image, table)


def find_paired_folders(directory):
    paired_folders = []
    folder_names = os.listdir(directory)

    images = {name for name in folder_names if name.endswith('_image')}
    gts = {name for name in folder_names if name.endswith('_gt')}

    common_names = images.intersection({name.replace('_gt', '_image') for name in gts})

    for common_name in common_names:
        paired_folders.append((common_name, common_name.replace('_image', '_gt')))

    return paired_folders


directory = root
paired_folders = find_paired_folders(directory)
gammas = [0.3030, 0.6060]
image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']

for image_folder, gt_folder in paired_folders:
    print(f'gamma变换中，{image_folder}配对的是{gt_folder}')
    for file_name in os.listdir(root + image_folder):
        file_path = os.path.join(root + image_folder, file_name)
        if os.path.isfile(file_path):
            image = cv2.imread(file_path)
            if image is not None:
                for gamma in gammas:
                    if not os.path.exists(root + f'gamma{gamma:.4f}_{image_folder}'):
                        os.makedirs(root + f'gamma{gamma:.4f}_{image_folder}')
                    corrected_image = adjust_gamma(image, gamma)
                    new_file_name = f'{file_name}'
                    cv2.imwrite(os.path.join(root, f'gamma{gamma:.4f}_{image_folder}', new_file_name), corrected_image)

    print(f'gt粘贴中，{image_folder}配对的是{gt_folder}')
    for gamma in gammas:
        if not os.path.exists(root + f'gamma{gamma:.4f}_{gt_folder}'):
            os.makedirs(root + f'gamma{gamma:.4f}_{gt_folder}')
        for filename in os.listdir(root + gt_folder):
            if any(filename.lower().endswith(ext) for ext in image_extensions):
                shutil.copy(os.path.join(root + gt_folder, filename), root + f'gamma{gamma:.4f}_{gt_folder}')

# 判断是否有空的文件夹
import os


def check_images_in_folders(parent_directory):
    for folder_name in os.listdir(parent_directory):
        folder_path = os.path.join(parent_directory, folder_name)
        if os.path.isdir(folder_path):  # 判断是否为文件夹
            image_count = len(
                [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff'))])
            if image_count != 200:
                print(f"Folder '{folder_path}' does not contain 200 images, but {image_count}")
            else:
                pass


# 使用示例
check_images_in_folders(root)
