# 获取最大三个值的索引
    top_3_indices = np.argsort(intensities)[-3:]
    
    # 倒序排列以确保第一个索引是最大值，其次是其次大值
    top_3_indices = top_3_indices[::-1]
    
    # 根据索引获取相应的点
    top_3_points = [coords[i] for i in top_3_indices] 
