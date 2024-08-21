# 移除批次维度，并转置到(高度, 宽度, 通道)格式
tensor = tensor.squeeze(0).permute(1, 2, 0)

# 将 tensor 转换为 numpy 数组并标准化到[0,255]
array = tensor.numpy()
array = 255 * (array - array.min()) / (array.max() - array.min())
array = array.astype(np.uint8)

# 创建 Pillow 图像并保存
image = Image.fromarray(array)
image.save("10_flip.png")

print(f"图像已保存为 '10_flip.png'")
