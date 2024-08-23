# 假设你的文本文件名为 'data.txt'
file_path = 'data.txt'

# 读取文件内容
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# 将读取的字符串内容转换成字典
dict_data = ast.literal_eval(content)
