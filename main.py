# 生成Excel列名
def get_excel_column_name(n):
    name = ''
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        name = chr(65 + remainder) + name
    return name

# 按照顺序将图像插入到H5、I5、J5以此类推
for index in range(20):
    image_path = os.path.join(image_folder, image_files[index])
    img = Image(image_path)
    col = get_excel_column_name(8 + index)  # 8对应H列
    img.anchor = f'{col}5'
    sheet.add_image(img)
