def set_parameter_requires_grad(model):
    for name, param in model.named_parameters():
        if not re.match(r'classifier.*', name):
            param.requires_grad = False
        else:
            param.requires_grad = True
