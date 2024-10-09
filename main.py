def overlay_significant_pixels(original_folder, ai_result_folder, output_folder, threshold=30):
    """
    将 original_folder 中像素值大于阈值的像素叠加到 ai_result_folder 中的图像上。

    :param original_folder: 包含原始图像的文件夹路径
    :param ai_result_folder: 包含 AI 结果图像的文件夹路径
    :param output_folder: 输出结果图像的文件夹路径
    :param threshold: 像素值阈值，默认为 30
    """
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    # 获取所有文件名
    original_files = sorted([f for f in os.listdir(original_folder) if f.endswith('.png')])
    ai_result_files = sorted([f for f in os.listdir(ai_result_folder) if f.endswith('.png')])

    for original_file, ai_result_file in zip(original_files, ai_result_files):
        original_path = os.path.join(original_folder, original_file)
        ai_result_path = os.path.join(ai_result_folder, ai_result_file)
        
        original_image = Image.open(original_path).convert('RGBA')
        ai_result_image = Image.open(ai_result_path).convert('RGBA')
        
        # 创建一个新的图像，用于叠加结果
        overlay_image = ai_result_image.copy()
        
        original_pixels = original_image.load()
        overlay_pixels = overlay_image.load()
        
        for y in range(original_image.height):
            for x in range(original_image.width):
                # 检查像素值是否大于阈值
                if max(original_pixels[x, y][:3]) > threshold:
                    overlay_pixels[x, y] = original_pixels[x, y]
        
        # 保存结果文件
        overlay_image.save(os.path.join(output_folder, original_file.replace('_original', '_overlay')))

    print("操作完成，每对图像已处理并保存。")
