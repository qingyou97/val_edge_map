import numpy as np
import torch

def generate_sinusoidal_position_encoding(batch_size, height, width, num_channels, device):
    def get_angles(pos, i, d_model):
        angle_rates = 1 / np.power(10000, (2 * (i // 2)) / np.float32(d_model))
        return pos * angle_rates

    angle_rads_x = get_angles(np.arange(width)[:, np.newaxis], np.arange(num_channels)[np.newaxis, :], num_channels)
    angle_rads_y = get_angles(np.arange(height)[:, np.newaxis], np.arange(num_channels)[np.newaxis, :], num_channels)

    # apply sin to even indices in the array; 2i
    angle_rads_x[:, 0::2] = np.sin(angle_rads_x[:, 0::2])
    angle_rads_y[:, 0::2] = np.sin(angle_rads_y[:, 0::2])

    # apply cos to odd indices in the array; 2i+1
    angle_rads_x[:, 1::2] = np.cos(angle_rads_x[:, 1::2])
    angle_rads_y[:, 1::2] = np.cos(angle_rads_y[:, 1::2])

    # Expand the positional encoding appropriately
    pos_encoding_x = torch.tensor(angle_rads_x[np.newaxis, :, :, np.newaxis], dtype=torch.float32).to(device)
    pos_encoding_y = torch.tensor(angle_rads_y[np.newaxis, :, :, np.newaxis], dtype=torch.float32).to(device)

    pos_encoding_x = pos_encoding_x.expand(batch_size, height, -1, num_channels)
    pos_encoding_y = pos_encoding_y.expand(batch_size, width, -1, num_channels)

    # permute to fit dimensions and concatenate
    pos_encoding_x = pos_encoding_x.permute(0, 3, 1, 2)
    pos_encoding_y = pos_encoding_y.permute(0, 3, 2, 1)
    
    pos_encoding = torch.cat((pos_encoding_x, pos_encoding_y), dim=1)
    # Ensure pos_encoding has the correct dimension to concatenate with x
    return pos_encoding
