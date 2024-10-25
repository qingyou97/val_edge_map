start_x = rect[0][0]
end_x = rect[1][0]

for i in range(start_x, end_x + 1):
    line = list(range(i, i + 5))
    if line[-1] > end_x + 1:
        break
    print(line)
