import random
import string

def generate_random_string(length):
    letters = string.ascii_letters + string.digits  # 包含字母和数字
    return ''.join(random.choice(letters) for i in range(length))

# 生成一个长度为10的随机字符串
random_string = generate_random_string(10)
