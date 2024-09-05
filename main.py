# 学习率下降策略
        if epoch + 1 > 70:
            for param_group in optimizer.param_groups:
                param_group['lr'] = 0.1 * param_group['lr']
