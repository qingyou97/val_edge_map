from PIL import Image

# 打开黑白图像
img = Image.open('A图.png').convert('RGBA')

# 定义颜色替换规则
color_mapping = {
    (255, 255, 255, 255): (253, 231, 36, 255),
    (0, 0, 0, 255): (68, 1, 84, 255)
}

# 获取图像数据
data = img.getdata()

# 创建一个新的图像数据列表
new_data = []
for item in data:
    if item in color_mapping:
        new_data.append(color_mapping[item])
    else:
        new_data.append(item)

# 创建新的图像对象并赋予新的数据
new_img = Image.new("RGBA", img.size)
new_img.putdata(new_data)

# 保存为新的PNG图像
new_img.save('A图_new.png')
