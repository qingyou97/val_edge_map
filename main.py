import os
import fnmatch

def find_non_jpg_files(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            if not fnmatch.fnmatch(filename, '*.jpg'):
                print("Non-JPG file found:", os.path.join(root, filename))

folder_path = 'your_directory_path_here'
find_non_jpg_files(folder_path)
