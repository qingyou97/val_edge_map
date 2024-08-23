import os
from PIL import Image
import numpy as np

def image_to_array(image_path):
    image = Image.open(image_path)
    return np.array(image)

def main():
    folder_a = 'path/to/A_folder'  # 替换为A文件夹的路径
    folder_b = 'path/to/B_folder'  # 替换为B文件夹的路径

    images_a = {file:image_to_array(os.path.join(folder_a, file)) for file in os.listdir(folder_a) if os.path.isfile(os.path.join(folder_a, file))}
    images_b = {file:image_to_array(os.path.join(folder_b, file)) for file in os.listdir(folder_b) if os.path.isfile(os.path.join(folder_b, file))}

    to_delete = []
    for file_b, image_b in images_b.items():
        for image_a in images_a.values():
            if np.array_equal(image_a, image_b):
                to_delete.append(os.path.join(folder_b, file_b))
                break
    
    for file in to_delete:
        os.remove(file)
        print(f"Deleted: {file}")

if __name__ == "__main__":
    main()
