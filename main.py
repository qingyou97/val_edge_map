import sys

class OutputToFile:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.file = open(filename, 'w')

    def write(self, message):
        self.terminal.write(message)
        self.file.write(message)

    def flush(self):
        self.terminal.flush()

# 重定向标准输出到文件
sys.stdout = OutputToFile('output.txt')

# 现在的print语句会同时输出到控制台和文件中
print("Hello, world!")
print("This will be written to both console and the output.txt file.")

# 恢复标准输出
sys.stdout.file.close()
sys.stdout = sys.stdout.terminal
