# 读取并调整图像大小
    image_path = os.path.join(target_folder_path, image_name)
    img = PilImage.open(image_path)
    img = img.resize((100, 100))  # 调整图像大小为100x100像素
    img.save('resized_image.png')  # 保存调整后的图像
    
    # 粘贴调整后的图像
    resized_img = OpenpyxlImage('resized_image.png')
    resized_img.anchor = f'{col_letter}{row}'
    sheet.add_image(resized_img)  # 粘贴图像到该单元格后面
