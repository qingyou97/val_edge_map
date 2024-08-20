import random
import string

def generate_random_name(length):
    letters = string.ascii_letters  # 包含所有大小写字母
    return ''.join(random.choice(letters) for _ in range(length))

name_length = 10  # 你可以改变名字的长度
random_name = generate_random_name(name_length)
print("生成的随机名字是：", random_name)
