process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')

# 实时输出标准输出
for stdout_line in iter(process.stdout.readline, ''):
    print(stdout_line, end='')

# 实时输出标准错误
for stderr_line in iter(process.stderr.readline, ''):
    print(stderr_line, end='')

process.stdout.close()
process.stderr.close()

return_code = process.wait()
print(f"Return Code: {return_code}")

if return_code != 0:
    print(f"Command failed: {command}")
