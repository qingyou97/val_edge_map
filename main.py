cropped_img_300 = img.crop((left, top, right, bottom))
        result_filename = f"{os.path.splitext(filename)[0]}_result{os.path.splitext(filename)[1]}"
        cropped_img_300.save(os.path.join(B_folder, result_filename))

        # 保留1200-1500像素
        left = 1200
        right = 1500 if width >= 1500 else width
        if width >= 1200:
            cropped_img_1200_1500 = img.crop((left, top, right, bottom))
            original_filename = f"{os.path.splitext(filename)[0]}_original{os.path.splitext(filename)[1]}"
            cropped_img_1200_1500.save(os.path.join(B_folder, original_filename))

print("所有图片已裁剪并保存到B文件夹。")
