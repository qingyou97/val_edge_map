from PIL import Image
import os

def process_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        if filename.endswith('.png'):
            img = Image.open(file_path).convert('L')
            img_resized = img.resize((512, 512), Image.BICUBIC)
            img_resized = img_resized.point(lambda p: 255 if p > 0 else 0)
            img_resized.save(os.path.join(output_folder, filename), 'PNG')
        
        elif filename.endswith('.jpg'):
            img = Image.open(file_path)
            img_resized = img.resize((512, 512), Image.BICUBIC)
            img_resized.save(os.path.join(output_folder, filename), 'JPEG')

input_folder = 'path/to/your/input/folder'
output_folder = 'path/to/your/output/folder'

process_images(input_folder, output_folder)
