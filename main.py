      
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows


# 数据字典

def dict2excel(dict1, sheet_name, excel_path):
    # 将字典转换为 DataFrame
    data = {'id': [], 'model': [], 'precision': [], 'recall': [], 'f1': []}
    for key, val in dict1.items():
        data['id'].append(key)
        data['model'].append(val['save_path'].split('/')[-1])
        data['precision'].append(val['precision'])
        data['recall'].append(val['recall'])
        data['f1'].append(val['f1'])

    df = pd.DataFrame(data)


    wb = Workbook()
    ws = wb.active
    ws.title = sheet_name  # 重命名

    # 将 DataFrame 写入 "Sheet 3"
    for r in dataframe_to_rows(df, index=False, header=True):
        ws.append(r)

    # 保存 Excel 文件
    wb.save(excel_path)

    print("已成功将字典数据写入 Excel 文件")

if __name__ == '__main__':
    dict1 = {
        1: {
            'save_path': 'D:\\\\edge_detection\\\\code\\\\pidinet-master\\\\result_for_loop/1-Aero-engine-defect/14_2_checkpoint_100',
            'precision': 0.09705242806814462, 'recall': 0.13762851637899637, 'f1': 0.10879137458647996},
        2: {
            'save_path': 'D:\\\\edge_detection\\\\code\\\\pidinet-master\\\\rresult_for_loop/1-Aero-engine-defect/14_2_checkpoint_200',
            'precision': 0.09392229472958573, 'recall': 0.17632804550567358, 'f1': 0.11746023553192468},
        3: {
            'save_path': 'D:\\\\edge_detection\\\\code\\\\pidinet-master\\\\¥result_for_loop/1-Aero-engine-defect/14_2_checkpoint_299',
            'precision': 0.076702883047196, 'recall': 0.2024797227578691, 'f1': 0.10737306906407429}
    }
    excel_path = 'out.xlsx'
    dict2excel(dict1, 'name', excel_path)

    
