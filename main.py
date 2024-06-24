import os

def get_file_stems(directory, extension):
    return {os.path.splitext(file)[0] for file in os.listdir(directory) if file.endswith(extension)}

def check_corresponding_files(folder_a, ext_a, folder_b, ext_b):
    stems_a = get_file_stems(folder_a, ext_a)
    stems_b = get_file_stems(folder_b, ext_b)
    return stems_a == stems_b

folder_a = "A文件夹路径"
folder_b = "B文件夹路径"

if check_corresponding_files(folder_a, ".jpg", folder_b, ".png"):
    print("文件名一一对应")
else:
    print("文件名不对应")
