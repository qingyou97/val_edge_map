def generate_excel_columns(start_column='AD'):
    columns = []
    start_ord = ord(start_column[0]) * 26 + ord(start_column[1]) - 16384
    
    for i in range(start_ord, 16384):  # 16384 corresponds to 'XFD' column
        if i < 26:
            columns.append(chr(i + ord('A')))
        else:
            columns.append(chr(i // 26 - 1 + ord('A')) + chr(i % 26 + ord('A')))
    
    return columns

columns = generate_excel_columns(start_column='AD')
