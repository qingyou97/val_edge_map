class FeatureExtractor(nn.Module):
    def __init__(self, num_classes):
        super(FeatureExtractor, self).__init__()

        self.conv = nn.Conv2d(128, 1, kernel_size=3, stride=1, padding=1)

    def forward(self, middle_output_list):
        upsampled_map_list = []
        for i, map in enumerate(middle_output_list):
            upsampled_map = F.interpolate(map, size=(512, 512), mode='nearest', align_corners=False)
            upsampled_map_list.append(upsampled_map)
        upsampled_map_cat = torch.cat(upsampled_map_list, dim=1)
        map = self.conv(upsampled_map_cat)

        return map
