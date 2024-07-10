在`cv2.Canny()`中，阈值用于边缘检测的步骤：

1. **低阈值**：第一阈值。低于这个值的像素会被认为不是边缘，直接滤除。
2. **高阈值**：第二阈值。高于这个值的像素会被认为是确定的边缘。
3. **双阈值**：介于两个阈值之间的像素根据与已确定边缘的连通性来判断是否为边缘。
