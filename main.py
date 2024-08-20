from PIL import Image

# 转换pyl浮数组为image对象
image = Image.fromarray(lb.astype(np.uint8))

# 保存为图像文件
image.save('output_image.png')
