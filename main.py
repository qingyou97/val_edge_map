import os

def get_file_stems(directory, extension):
    return {os.path.splitext(file)[0] for file in os.listdir(directory) if file.endswith(extension)}

def are_filenames_corresponding(folder_a, ext_a, folder_b, ext_b):
    stems_a = get_file_stems(folder_a, ext_a)
    stems_b = get_file_stems(folder_b, ext_b)
    
    only_in_a = stems_a - stems_b
    only_in_b = stems_b - stems_a
    
    return only_in_a, only_in_b

folder_a = "A文件夹路径"
folder_b = "B文件夹路径"

only_in_a, only_in_b = are_filenames_corresponding(folder_a, ".jpg", folder_b, ".png")

if not only_in_a and not only_in_b:
    print("文件名一一对应")
else:
    if only_in_a:
        print("以下文件只在A文件夹中存在:", only_in_a)
    if only_in_b:
        print("以下文件只在B文件夹中存在:", only_in_b)
