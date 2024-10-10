# 检查文件是否存在
if not os.path.exists(file_path):
    # 创建一个新的工作簿
    workbook = openpyxl.Workbook()
    # 保存工作簿
    workbook.save(file_path)
    print(f"文件 {file_path} 已创建。")
else:
    print(f"文件 {file_path} 已存在。")
