import sys

def main():
    # 你的代码开始
    print("这是你的代码中的print语句1")
    print("这是你的代码中的print语句2")
    # 你的代码结束

# 打开log.txt文件
log_file = open('log.txt', 'a')

# 保存原始的sys.stdout
original_stdout = sys.stdout

# 重定向sys.stdout到log_file
sys.stdout = log_file

# 执行你的代码
main()

# 恢复原始的sys.stdout
sys.stdout = original_stdout

# 关闭log文件
log_file.close()

# 现在print会输出到控制台
print("这是普通的print输出")
