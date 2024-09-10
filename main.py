# 将 a 作为输入传给模型
    output = model.forward(a)

    # 如果你想打打印出所有输出，可以使用以下循环进行打印：
    for i, out in enumerate(output):
        print(f'Output {i}: {out.size()}')
        print(out)
