inner_radius = 1  # 设定inner_radius
outer_radius = 5  # 设定outer_radius
rect_width = 10   # 设定rect_width
length = 5        # 要取出的序列长度

for i in range(rect_width + 1):
    sequence = [(j + i) % (rect_width + 1) for j in range(length)]
    for x in sequence:
        for y in range(inner_radius, outer_radius + 1):
            print((x, y))
