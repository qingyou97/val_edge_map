# 假设 command 和 current_dir 是定义好的
command = ["your_command_here"]  # 根据实际命令调整
current_dir = "D:\\\\your_path_here"  # 确保路径合法并存在

# 运行命令
try:
    result = subprocess.run(command, cwd=current_dir, check=True, capture_output=True, text=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
