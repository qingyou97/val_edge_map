for x in range(rect_width + 1):
    sequence = [(j + x) % (rect_width + 1) for j in range(length)]
    for y in range(inner_radius, outer_radius + 1):
        for value in sequence:
            print((value, y))
