def annotate_and_save_image(img, peak_coordinates, output_path):
    annotated_img = img.copy()
    for y, x, _ in peak_coordinates:
        cv2.circle(annotated_img, (x, y), 5, (0, 0, 255), -1)  # 红色圆圈
        cv2.putText(annotated_img, f"({x},{y})", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

    cv2.imwrite(output_path, annotated_img)
# 标注并保存图像
output_path = os.path.join(folder_path, f"annotated_{filename}")
annotate_and_save_image(img, peak_coordinates, output_path)
