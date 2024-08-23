def generate_excel_columns(start_column):
    columns = []
    
    # Calculate the starting ordinal value based on the length of the start_column
    if len(start_column) == 1:
        start_ord = ord(start_column[0]) - ord('A')
    elif len(start_column) == 2:
        start_ord = (ord(start_column[0]) - ord('A') + 1) * 26 + ord(start_column[1]) - ord('A')
    elif len(start_column) == 3:
        start_ord = ((ord(start_column[0]) - ord('A') + 1) * 26 + (ord(start_column[1]) - ord('A') + 1)) * 26 + ord(start_column[2]) - ord('A')
    else:
        raise ValueError("Invalid start_column length")

    for i in range(start_ord, 16384):  # 16384 corresponds to 'XFD' column
        if i < 26:
            # Single letter column
            columns.append(chr(i + ord('A')))
        elif i < 702:  # AA to ZZ (26 + 26^2 - 26) = 702
            # Double letter column
            columns.append(chr(i // 26 - 1 + ord('A')) + chr(i % 26 + ord('A')))
        else:
            # Three letter column
            first = chr((i - 702) // 676 + ord('A'))
            second = chr(((i - 702) % 676) // 26 + ord('A'))
            third = chr((i - 702) % 26 + ord('A'))
            columns.append(first + second + third)
    
    return columns
