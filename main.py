# 设置字体
   font_path = "C:/Windows/Fonts/simsun.ttc"  # 这是Windows系统下的宋体路径
   font_prop = font_manager.FontProperties(fname=font_path)
   plt.rcParams['font.family'] = font_prop.get_name()
