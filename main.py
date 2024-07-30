import os
import re
import openpyxl
from PIL import Image
import shutil

def get_column_letter(n):
    """生成 Excel 列名"""
    result = ''
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        result = chr(65 + remainder) + result
    return result

def image2excel(excel_file_path, sheet_number, start_row_num,start_col_num, img_folder_path, width, height):
    # 配置文件夹路径和Excel路径
    folder_path = img_folder_path
    excel_path = excel_file_path
    sheet_name = sheet_number
    start_row = start_row_num
    start_col = start_col_num

    # 读取所有图像文件
    image_files = []
    for f in os.listdir(folder_path):
        if f.split('.')[-1] in ['png','jpg', 'jpeg']:
            image_files.append(f)

    # 按照文件名排序
    image_files.sort()
    print(f'image_files:{image_files}')

    # 打开Excel文件
    wb = openpyxl.load_workbook(excel_path)
    sheet = wb[sheet_name]
    ws = wb.active

    current_row = start_row
    curent_col = start_col

    # 新建文件夹保存缩略图
    s_img_folder = os.path.join(img_folder_path, 's_img_folder')
    if not os.path.exists(s_img_folder):
        os.makedirs(s_img_folder)

    # 遍历排序后的图像文件名，将其填入Excel文件并粘贴对应的图片
    for image_file in image_files:
        img_path = os.path.join(folder_path, image_file)

        # 写入图像名
        sheet.cell(row=current_row, column=curent_col, value=image_file)

        # 读取并粘贴图像
        img = Image.open(img_path)
        img.thumbnail((100, 100), Image.LANCZOS)

        path = os.path.join(s_img_folder, image_file)
        img.save(path)
        spreadsheet_img = openpyxl.drawing.image.Image(path) # f"{image_file}"
        sheet.add_image(spreadsheet_img, f"{get_column_letter(curent_col)}{current_row + 1}")

        # 设置列宽
        ws.column_dimensions[get_column_letter(curent_col)].width = width  # 设置 A 列宽度为20
        # 设置行高
        ws.row_dimensions[current_row+1].height = height  # 设置第1行高度为40

        curent_col += 1

    # 保存Excel文件
    wb.save(excel_path)

    if os.path.exists(s_img_folder) and os.path.isdir(s_img_folder):
        # 清空文件夹
        shutil.rmtree(s_img_folder)


if __name__ == '__main__':
    folder_path = r"E:\Datasets\Industrial quality inspection\CRACK500\valdata\valdata" # 存放图片的文件夹地址
    excel_path = r"E:\image2excel\1.xlsx"
    sheet_number = "Sheet1" # Sheet表名
    start_row_num = 3 # 起始行
    start_col_num = 1 # 起始列
    width = 20 # 单元格宽度
    height = 40 # 单元格高度
    image2excel(excel_path, sheet_number, start_row_num, start_col_num, folder_path,width, height)
