def overlay_original_on_ai_result(original_folder, ai_result_folder, output_folder):
    """
    将 original_folder 中的图像中的有值像素叠加到 ai_result_folder 中的图像上，以查看重合度。

    :param original_folder: 包含原始图像的文件夹路径
    :param ai_result_folder: 包含 AI 结果图像的文件夹路径
    :param output_folder: 输出结果图像的文件夹路径
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
                if original_pixels[x, y][3] != 0:  # 检查 alpha 通道是否不为 0
                    overlay_pixels[x, y] = original_pixels[x, y]
        
        # 保存结果文件
        overlay_image.save(os.path.join(output_folder, original_file.replace('_original', '_overlay')))

    print("操作完成，每对图像已处理并保存。")

# 使用示例
original_folder = 'A文件夹'
ai_result_folder = 'B文件夹'
output_folder = '叠加结果文件夹'
overlay_original_on_ai_result(original_folder, ai_result_folder, output_folder)
