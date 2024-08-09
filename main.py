# 打印当前的工作目录和环境变量
print(f"Current working directory: {os.getcwd()}")
print("Environment variables:")
for key, value in os.environ.items():
  print(f"{key}: {value}")

process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# 实时显示 log
while True:
    output = process.stdout.readline()
    if output == "" and process.poll() is not None:
        break
    if output:
        print(output.strip())

# 打印错误信息
stderr = process.stderr.read()
if stderr:
    print(f"Error: {stderr.strip()}")

return_code = process.poll()
print(f"Process finished with return code: {return_code}")
