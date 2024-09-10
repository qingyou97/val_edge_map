x2 = torch.nn.functional.interpolate(x2, size=(128, 128), mode='bilinear', align_corners=False)

        x = torch.cat((x1, x2), dim=1)
