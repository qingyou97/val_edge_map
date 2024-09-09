def forward(self, x):
        batch_size, _, h, w = x.shape
        
        # 生成网格
        pos_y, pos_x = torch.meshgrid(torch.linspace(0, 1, h), torch.linspace(0, 1, w))
        pos_x = pos_x.unsqueeze(0).unsqueeze(0).expand(batch_size, -1, -1, -1)  # (B, 1, H, W)
        pos_y = pos_y.unsqueeze(0).unsqueeze(0).expand(batch_size, -1, -1, -1)  # (B, 1, H, W)
        
        # 生成正弦余弦位置编码
        pos_x = pos_x * math.pi
        pos_y = pos_y * math.pi
        sin_encoding_x = torch.sin(pos_x)
        cos_encoding_x = torch.cos(pos_x)
        sin_encoding_y = torch.sin(pos_y)
        cos_encoding_y = torch.cos(pos_y)
        
        position_encoding = torch.cat([sin_encoding_x, cos_encoding_x, sin_encoding_y, cos_encoding_y], dim=1).to(x.device)  # (B, 4, H, W)
        
        x = torch.cat([x, position_encoding], dim=1)  # (B, 3+4, H, W)
        x = self.encoder(x)
        x = self.decoder(x)
        return x
