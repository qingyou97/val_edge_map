import subprocess

# 要运行的Python命令列表
commands = [
    'python script1.py',
    'python script2.py',
    'python script3.py',
    # ... 更多命令
    'python script10.py'
]

for command in commands:
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(f"Running: {command}")
    print(f"Return Code: {process.returncode}")
    print(f"Output: {process.stdout}")
    if process.stderr:
        print(f"Error: {process.stderr}")

    if process.returncode != 0:
        print(f"Command failed: {command}")
        break
