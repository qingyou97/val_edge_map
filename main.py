# Compute angle from A (y, x) to B (y2, x2)
    delta_y = y2 - y
    delta_x = x2 - x
    angle_rad = math.atan2(delta_y, delta_x)
    angle_deg = np.degrees(angle_rad)
    
    # The angle_deg should be in range [0, 180)
    angle_deg = angle_deg % 180
