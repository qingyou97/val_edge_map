def calculate_average(numbers):
    if not numbers:  # 检查列表是否为空
        return 0
    return sum(numbers) / len(numbers)
