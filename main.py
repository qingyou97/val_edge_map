import os
from PIL import Image

# Define the paths for folder A and folder B
a_folder = 'path/to/A_folder'
b_folder = 'path/to/B_folder'

# Ensure folder B exists, create it if it does not
if not os.path.exists(b_folder):
    os.makedirs(b_folder)

# Iterate over all files in folder A
for filename in os.listdir(a_folder):
    if filename.endswith('.png'):
        # Open the image
        img = Image.open(os.path.join(a_folder, filename))

        # Convert the image to grayscale (to prevent colored results)
        img = img.convert('L')

        # Invert the pixel values of the image (black to white, white to black)
        img_inverted = Image.eval(img, lambda x: 255 - x)
        
        # Save the modified image to folder B
        save_path = os.path.join(b_folder, filename)
        img_inverted.save(save_path)

print("Images have been converted and saved to folder B")
