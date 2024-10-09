def find_color_coordinates(image_path, target_color):
    image = Image.open(image_path).convert('RGBA')
    width, height = image.size
    pixels = image.load()

    coordinates = []

    for y in range(height):
        for x in range(width):
            if pixels[x, y] == target_color:
                coordinates.append((x, y))
    
    return coordinates
