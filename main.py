A = "字符串A"
B = "字符串B"
file_path = "输出文件.txt"

with open(file_path, "w", encoding="utf-8") as file:
    file.write(f"{A} {B}\
")
