import os

images = os.listdir(target_folder_path)
png_images = [image for image in images if image.endswith('.png')]
