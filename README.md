probabilities = torch.sigmoid(output) if net.n_classes == 1 else F.softmax(output, dim=1)
