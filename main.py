# 将字典内容写入txt文件
with open('result.txt', 'w') as file:
    file.write(str(result_dict))

print('字典内容已保存到result.txt文件中')
