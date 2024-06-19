def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# 示例列表
numbers = [1, 2, 3, 4, 5]

# 计算平均值
average = calculate_average(numbers)
print(f"列表的平均值是: {average}")
