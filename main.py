# 在左上角标注坐标
    text = f'({x},{y})'
    text_position = (5, 15 + coords.index(item) * 20)  # 计算每个坐标的文字位置，避免重叠
    cv2.putText(img_anno, text, text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
