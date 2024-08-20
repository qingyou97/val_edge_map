def write_image_paths_to_txt(folder_path, output_file):
    with open(output_file, 'w', newline='\
') as file:
        for root, dirs, files in os.walk(folder_path):
            for name in files:
                if name.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                    file.write(os.path.join(root, name) + '\
')
