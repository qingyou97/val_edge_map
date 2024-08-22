 image_path = os.path.join(target_folder_path, image_name)
    img = PilImage.open(image_path)
    img = img.resize((60, 60))
    
    unique_image_path = f'resized_image_{count}.png'
    img.save(unique_image_path)
    
    resized_img = OpenpyxlImage(unique_image_path)
    resized_img.anchor = f'{col_letter}{row}'
    sheet.add_image(resized_img)
