from PIL import Image
import numpy as np

# 加载A图、B图和C图
A_img = Image.open('A.png').convert('L')
B_img = Image.open('B.png').convert('L')
C_img = Image.open('C.png').convert('RGB')

# 将图像转换为numpy数组
A_array = np.array(A_img)
B_array = np.array(B_img)
C_array = np.array(C_img.copy())

# 创建一个新的图像数组
out_array = np.array(C_img)

# 定义颜色
white = [255, 255, 255]
red = [255, 0, 0]
blue = [0, 0, 255]

# 获取非零的（有效的）像素点
A_mask = A_array > 0
B_mask = B_array > 0
overlap_mask = A_mask & B_mask

# 将A和B图像中相应的像素点用指定颜色标记
out_array[A_mask & ~overlap_mask] = white
out_array[B_mask & ~overlap_mask] = red
out_array[overlap_mask] = blue

# 保存结果图像
out_img = Image.fromarray(out_array)
out_img.save('output.png')

# 打开生成的新图像
out_img.show()
