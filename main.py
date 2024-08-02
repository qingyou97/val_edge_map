def resize_image(image, max_size):
    _, _, H, W = image.shape
    if H > max_size or W > max_size:
        scaling_factor = max_size / float(max(H, W))
        new_H = int(H * scaling_factor)
        new_W = int(W * scaling_factor)
        image = F.interpolate(image, size=(new_H, new_W), mode='bilinear', align_corners=False)
    return image
