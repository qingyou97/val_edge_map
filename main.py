rect_width = 10  # 这里设定你的最大值
length = 5  # 要取出的序列长度

for i in range(rect_width + 1):
    sequence = [(j + i) % (rect_width + 1) for j in range(length)]
    print(sequence)
