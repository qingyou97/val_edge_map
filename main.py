try:
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # 实时显示log
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

except Exception as e:
    print(f"An error occurred: {e}")
