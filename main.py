import os

def ensure_path_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

path = 'your/directory/path'
ensure_path_exists(path)
