for i in range(rect_width + 1):
    sequence = [(j + i) % (rect_width + 1) for j in range(length)]
    for x in sequence:
        for y in range(inner_radius, outer_radius + 1):
            print((x, y))
