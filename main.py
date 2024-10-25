# 提高所有坐标点的对比度（比如亮度翻倍，使用clipping避免溢出）
   for (x, y) in coordinates:
       image[y, x] = min(255, image[y, x] * 2)
