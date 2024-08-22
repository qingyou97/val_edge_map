import random
import string
import time

def generate_random_string_with_timestamp(length):
    letters = string.ascii_letters + string.digits
    random_part = ''.join(random.choice(letters) for i in range(length))
    timestamp = str(int(time.time() * 1000))  # 毫秒级时间戳
    return random_part + timestamp

# 生成一个包含时间戳的随机字符串
random_string = generate_random_string_with_timestamp(10)
