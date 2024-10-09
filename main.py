magnitude_save = np.uint8(np.clip(magnitude / magnitude.max() * 255, 0, 255))
    cv2.imwrite('edge_magnitude.png',magnitude_save)
