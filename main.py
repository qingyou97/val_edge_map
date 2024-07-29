def is_image(file_path):
    try:
        Image.open(file_path).verify()
        return True
    except (IOError, SyntaxError):
        return False
