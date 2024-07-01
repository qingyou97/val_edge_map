import os

folder_path = 'test'
lst_file_path = 'lst'

with open(lst_file_path, 'w') as lst_file:
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            lst_file.write(f'test/{file_name}.jpg\
')
