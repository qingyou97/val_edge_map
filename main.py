def get_sinusoidal_position_encoding(batch_size, h, w, d_model, device):
    pe = torch.zeros(h, w, d_model, device=device)

    y_position = torch.arange(0, h, dtype=torch.float, device=device).unsqueeze(1).repeat(1, w)
    x_position = torch.arange(0, w, dtype=torch.float, device=device).unsqueeze(0).repeat(h, 1)

    div_term = torch.exp(torch.arange(0, d_model, 2, dtype=torch.float, device=device) *
                         -(math.log(10000.0) / d_model))

    pe[:, :, 0::2] = torch.sin(y_position.unsqueeze(-1) * div_term)
    pe[:, :, 1::2] = torch.cos(x_position.unsqueeze(-1) * div_term)

    pe = pe.unsqueeze(0).expand(batch_size, -1, -1, -1)  # (B, H, W, D)
    return pe.permute(0, 3, 1, 2)  # (B, D, H, W)
