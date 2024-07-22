import torch
import torch.nn as nn
from unet.unet_model import UNet
import torch_pruning as tp
from import predict_images


def prune_unet(pt_path, save_path, test_images_path, results_base_model_path, results_pruned_model_path,norm_p, prune_ratio ):
    # 加载模型
    model = UNet(n_channels=3, n_classes=1)
    checkpoint = torch.load(pt_path, map_location=torch.device('cpu'))
    model.load_state_dict(checkpoint)
    print(f'before pruning:')
    print(model)

    prune_layers = []
    ignored_layers = []
    for name, module in model.named_children():
        print(name)

    for name, module in model.named_children():
        # set pruned model name
        if name not in ['up1', 'up2', 'up3', 'up4', 'outc']:
            # print(f"Name: {name}, Module: {module}")
            ignored_layers.append(module)
        else:
            prune_layers.append(module)

    # Importance criteria
    example_inputs = torch.randn(1, 3, 224, 224)

    # imp = tp.importance.GroupTaylorImportance()
    imp = tp.importance.MagnitudeImportance(p=norm_p)

    iterative_steps = prune_steps  # progressive pruning
    pruner = tp.pruner.MetaPruner(
        model,
        example_inputs,
        importance=imp,
        iterative_steps=iterative_steps,
        pruning_ratio=prune_ratio,
        ignored_layers=ignored_layers,
    )

    base_macs, base_nparams = tp.utils.count_ops_and_params(model, example_inputs)
    for i in range(iterative_steps):
        pruner.step()
        macs, nparams = tp.utils.count_ops_and_params(model, example_inputs)
        print(f'before base_nparams:{base_nparams}, base_macs:{base_macs}')
        print(f'after nparams:{nparams}, macs:{macs} ')
    print(f'after pruning:')
    print(model)

    # 4. save & load the pruned model

    torch.save(model, save_path)  # save the model object
    # model_loaded = torch.load(pruned_model_path, map_location=torch.device('cpu')) # no load_state_dict
    print('保存成功！')


    # 测试原模型
    predict_images(pt_path, test_images_path, results_base_model_path)
    print('原模型测试成功')
    # 测试剪枝模型
    predict_images(save_path,test_images_path, results_pruned_model_path)
    print('剪枝模型测试成功')




if __name__ == '__main__':
    pt_path = r'E:\pruning\CODE\Pytorch-UNet-master\weights\unet_carvana_scale1.0_epoch2.pth' # 原模型存放路径
    save_path = r'E:\pruning\CODE\Pytorch-UNet-master\weights\pruned_model.pth' # 新模型存放路径

    test_images_path = r'' # 测试图像路径
    results_base_model_path = r'' # 原模型测试结果存放路径
    results_pruned_model_path = r'' # 剪枝后模型测试结果存放路径

    norm_p = 2 # 针对MagnitudeImportance和GroupNormImportance
    prune_ratio = 0.5 # 修剪通道比例
    prune_steps = 5 # 修剪的迭代次数
    prune_unet(pt_path, save_path, test_images_path, results_base_model_path, results_pruned_model_path,norm_p, prune_ratio )
