# 定义命令和参数
command = [
    'python', 'train.py',
    '--batch-size', '1',
    '--param-dir', r'D:\\duan\\BDCN\\trained_model\\1-Aero-engine-defect\\14_2',
    '--max-itter', '15',
    '--data_lst', r'D:\\duan\\BDCN\\train_data\\1-Aero-engine-defect\\14_2\\train_pair.lst',
    '-c', '-g', '0'
]

# 获取当前脚本的目录
current_dir = os.path.dirname(__file__)

try:
    # 运行命令
    result = subprocess.run(command, cwd=current_dir, check=True, capture_output=True, text=True)
    # 打印标准输出
    print(result.stdout)
except subprocess.CalledProcessError as e:
    # 打印错误信息
    print(f"Error: {e.stderr}")
